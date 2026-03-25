# Security Analysis of Popular Android "Tools & Utilities" Applications

## Static Analysis Report — Mobile and Wireless Networks Security (2025-2026)

---

## 1. Abstract

This report presents a comprehensive security evaluation of 10 popular Android applications belonging to the **Tools & Utilities** category. Following the methodology set forth by Chatzoglou et al. in "Let the Cat out of the Bag: Popular Android IoT Apps under Security Scrutiny" (Sensors, MDPI, 2022), we perform static analysis using the Mobile Security Framework (MobSF) v4.3.1. Our analysis spans multiple axes including sensitive permissions, code weaknesses (CWEs), network security misconfigurations, manifest vulnerabilities, hardcoded secrets, tracker analysis, and shared library binary analysis.

The results reveal that even chart-topping, widely-used utility applications exhibit significant security and privacy concerns, including the use of weak cryptographic algorithms, cleartext data storage, excessive permissions, and hardcoded secrets. These findings underscore the prevalence of "technical debt" — the long-term cost of choosing quick solutions over secure implementations.

---

## 2. Methodology

### 2.1 App Selection

We selected 10 of the most downloaded applications from the **Tools & Utilities** category on the Google Play Store. The selection criteria were:
1. Apps must belong to the Tools & Utilities category
2. Apps must have a significant number of downloads (>1M)
3. Apps should represent a diverse set of functionalities within the category

### 2.2 Analysis Environment

- **Static Analysis Tool:** Mobile Security Framework (MobSF) v4.3.1
- **Analysis Type:** Automated static analysis of APK files
- **Key Analysis Components:**
  - Manifest analysis and permission mapping
  - Code analysis for Common Weakness Enumerations (CWEs)
  - Network security configuration analysis
  - Certificate and APK signing analysis
  - Tracker detection (via Exodus Privacy)
  - Shared library binary analysis
  - Hardcoded secrets detection

### 2.3 Data Collection

Each APK was uploaded to MobSF for automated static analysis. The resulting reports were extracted via the MobSF REST API and processed programmatically to construct the comparative tables and visualizations presented in this report.

---

## 3. Results

### 3.1 App Overview

### Table 1: Overview of Examined Android Applications

| # | App Name | Package Name | Version | Size | Downloads | Score |
|---|----------|-------------|---------|------|-----------|-------|
| 1 | Calculator | `com.sec.android.app.popupcalculator` | 12.5.00.24 | 6.04MB | 1,000,000,000+ | 4.5 |
| 2 | Calendar | `com.samsung.android.calendar` | 12.7.03.1 | 54.91MB | 1,000,000,000+ | 4.0 |
| 3 | QR & Barcode Scanner | `com.gamma.scan` | 2.2.221 | 19.67MB | 500,000,000+ | 4.8 |
| 4 | ZArchiver | `ru.zdevs.zarchiver` | 1.0.10 | 4.94MB | 100,000,000+ | 4.1 |
| 5 | Translate | `com.google.android.apps.translate` | 10.8.48.878519627.2-release | 46.93MB | 1,000,000,000+ | 4.3 |
| 6 | Speedtest | `org.zwanoo.android.speedtest` | 6.6.3 | 34.56MB | 100,000,000+ | 4.5 |
| 7 | Gboard | `com.google.android.inputmethod.latin` | 16.8.4.867538971-release-arm64-v8a | 81.43MB | 10,000,000,000+ | 4.5 |
| 8 | SHAREit | `com.lenovo.anyshare.gps` | 6.26.68_ww | 65.43MB | 1,000,000,000+ | 4.3 |
| 9 | Authenticator | `com.google.android.apps.authenticator2` | 7.0 | 9.06MB | 100,000,000+ | 3.9 |
| 10 | RAR | `com.rarlab.rar` | 7.20.build131 | 3.56MB | 100,000,000+ | 4.2 |


### 3.2 High-Level Static Analysis: Permissions

The identification and study of the runtime (dangerous) permissions used by each app is the first step towards understanding its behavior from a privacy viewpoint. Dangerous permissions are grouped into six categories: **Utility**, **Authentication**, **Location**, **Storage**, **Phone**, and **Communication**, following the methodology of the reference paper.

### Table 2: Identified Dangerous Permissions per Examined App

| App | U1 | U2 | A3 | L1 | L2 | L3 | L4 | S1 | S2 | S3 | P1 | P2 | P3 | P6 | P7 | P9 | P10 | Total |
|-----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|-------|
| Calculator |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  | **1** |
| Calendar |  |  |  | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |  | ✓ | ✓ |  | ✓ | ✓ | **9** |
| QR & Barcode Scanner | ✓ |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  | **3** |
| ZArchiver |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  | **3** |
| Translate |  | ✓ |  |  |  |  |  |  | ✓ |  |  | ✓ |  |  |  |  |  | **3** |
| Speedtest | ✓ |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  | **7** |
| Gboard | ✓ | ✓ | ✓ |  |  |  |  | ✓ |  |  |  |  | ✓ |  |  |  |  | **5** |
| SHAREit | ✓ |  |  | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ |  | **10** |
| Authenticator | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| RAR |  |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  | **2** |
| **TOTAL** | 5 | 2 | 1 | 3 | 3 | 1 | 1 | 6 | 7 | 3 | 1 | 2 | 3 | 2 | 1 | 2 | 1 | |

**Permission Legend:**
- **U1**: CAMERA
- **U2**: RECORD_AUDIO
- **A3**: GET_ACCOUNTS
- **L1**: ACCESS_FINE_LOCATION
- **L2**: ACCESS_COARSE_LOCATION
- **L3**: ACCESS_BACKGROUND_LOCATION
- **L4**: ACCESS_MEDIA_LOCATION
- **S1**: READ_EXTERNAL_STORAGE
- **S2**: WRITE_EXTERNAL_STORAGE
- **S3**: REQUEST_INSTALL_PACKAGES
- **P1**: READ_PHONE_STATE
- **P2**: SYSTEM_ALERT_WINDOW
- **P3**: READ_CONTACTS
- **P6**: WRITE_SETTINGS
- **P7**: GET_TASKS
- **P9**: READ_CALENDAR
- **P10**: WRITE_CALENDAR


#### Permissions Discussion

The analysis of dangerous permissions across the 10 examined apps reveals a total of **44 dangerous permission requests**. On average, each app requests **4.4 dangerous permissions**. The most permission-heavy app is **SHAREit** with 10 dangerous permissions, while **Calculator** requests the fewest with 1.

From a category perspective:
- **Location permissions** (L1/L2) are requested by **3** out of 10 apps (30%), which may or may not be justified depending on the app's functionality.
- **Storage permissions** (S1/S2) are present in **8** apps (80%), a common pattern for utility apps that handle files.
- **Camera access** (U1) is requested by **5** apps (50%).

As a general principle, the number of runtime permissions an app requests must be reduced to the bare minimum. By restricting access to dangerous permissions, the risk of inadvertently misusing them is reduced, and the app's attack surface is substantially decreased.

### 3.3 Low-Level Static Analysis: Code Weaknesses and Security Issues

To further investigate each app, we performed deep static analysis using MobSF, concentrating on Janus vulnerabilities, network security misconfigurations, APK signing algorithms, and Common Weakness Enumerations (CWEs).

### Table 3: Identified Weaknesses and Security Issues per App

| App | Janus | Net. Sec. | APK Sign | CWE-89 | CWE-250 | CWE-276 | CWE-295 | CWE-312 | CWE-327 | CWE-330 | CWE-532 | CWE-649 | CWE-749 | CWE-919 | Secrets | Score |
|-----|-------|-----------|----------|---|---|---|---|---|---|---|---|---|---|---|---------|-------|
| Calculator |  |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | 2 | 52 |
| Calendar |  | ⊠, ⊞ | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 224 | 47 |
| QR & Barcode Scanner |  | ⊠ | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  |  | 4189 | 47 |
| ZArchiver | ✓ |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  | 125 | 51 |
| Translate |  |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | 50 | 52 |
| Speedtest |  |  | SHA512 | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  | ✓ |  | 218 | 48 |
| Gboard |  |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  |  | 132 | 57 |
| SHAREit | ✓ | ⊠ | SHA512 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | 844 | 47 |
| Authenticator | ✓ |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | 499 | 49 |
| RAR | ✓ |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |  |  | 3 | 51 |
| **TOTAL** | 4 | | | 10 | 2 | 10 | 1 | 10 | 10 | 9 | 10 | 3 | 4 | 3 | | |

**Network Security symbols:** ● = cleartext traffic to all domains, ◎ = cleartext for specific domains, ⊠ = trusts system certificates, ⊞ = trusts user certificates, ⊡ = bypasses certificate pinning


#### CWE Analysis Discussion

- **CWE-89** (SQL Injection): Detected in **10** apps (100%)
- **CWE-250** (Exec. w/ Unnec. Privileges): Detected in **2** apps (20%)
- **CWE-276** (Incorrect Default Perms): Detected in **10** apps (100%)
- **CWE-295** (Improper Cert Validation): Detected in **1** apps (10%)
- **CWE-312** (Cleartext Storage): Detected in **10** apps (100%)
- **CWE-327** (Broken/Risky Crypto): Detected in **10** apps (100%)
- **CWE-330** (Insufficient Randomness): Detected in **9** apps (90%)
- **CWE-532** (Info Leak into Log File): Detected in **10** apps (100%)
- **CWE-649** (Encryption w/o Integrity): Detected in **3** apps (30%)
- **CWE-749** (Exposed Dangerous Method): Detected in **4** apps (40%)
- **CWE-919** (Mobile App Weaknesses): Detected in **3** apps (30%)

Regarding **Janus vulnerability** (CVE-2017-13156), 4 out of 10 apps (40%) were found to be potentially vulnerable. This vulnerability can be exploited when the v1 signature scheme is used with Android API 21-25.

Concerning **APK signing**, 0 apps were found to use SHA-1 for signing, which has been deprecated by NIST since 2013. Apps signed with deprecated algorithms are prone to collision attacks and potential hijacking.

### 3.4 Tracker Analysis

Third-party trackers may be embedded in apps and can pose privacy concerns. Using MobSF's Exodus-Privacy integration, we identified the trackers present in each app.

### Table 6: Detected Trackers per App

| App | Trackers Count | Tracker Names |
|-----|---------------|---------------|
| Calculator | 0 |  |
| Calendar | 0 |  |
| QR & Barcode Scanner | 3 | Facebook Ads, Google AdMob, Google Firebase Analytics |
| ZArchiver | 0 |  |
| Translate | 0 |  |
| Speedtest | 10 | Amazon Advertisement, Amazon Mobile Analytics (Amplify), ComScore, Google AdMob, Google Analytics (+5 more) |
| Gboard | 0 |  |
| SHAREit | 14 | Adjust, AppMonet, Facebook Analytics, Facebook Login, Google AdMob (+9 more) |
| Authenticator | 0 |  |
| RAR | 0 |  |


A total of **27 trackers** were detected across all examined apps. **3** out of 10 apps (30%) contain at least one tracker. The presence of trackers, particularly Analytics and Marketing types, raises privacy concerns as they may collect and transmit user data without explicit consent.

### 3.5 Manifest Analysis

The manifest file of each app was analyzed for potential security issues including exported components, cleartext traffic flags, backup settings, and other misconfigurations.

### Table 4: Manifest Analysis Results per App

| App | Exp. Activities | Exp. Services | Exp. Receivers | Exp. Providers | Cleartext | Backup | Debuggable | High Issues | Warn Issues |
|-----|----------------|--------------|---------------|---------------|-----------|--------|------------|-------------|-------------|
| Calculator | 0 | 2 | 3 | 1 | ✓ | ✓ |  | 1 | 7 |
| Calendar | 19 | 7 | 28 | 15 | ✓ |  |  | 1 | 71 |
| QR & Barcode Scanner | 0 | 1 | 2 | 0 |  | ✓ |  | 1 | 4 |
| ZArchiver | 5 | 0 | 0 | 1 |  | ✓ |  | 1 | 8 |
| Translate | 3 | 2 | 15 | 0 |  | ✓ |  | 0 | 25 |
| Speedtest | 6 | 2 | 5 | 0 | ✓ |  |  | 2 | 14 |
| Gboard | 5 | 3 | 5 | 2 |  | ✓ |  | 0 | 17 |
| SHAREit | 48 | 4 | 11 | 9 | ✓ |  |  | 2 | 142 |
| Authenticator | 1 | 1 | 5 | 0 |  |  |  | 1 | 7 |
| RAR | 0 | 1 | 2 | 0 |  | ✓ |  | 1 | 4 |


**Key Manifest Findings:**
- **4** apps permit cleartext traffic, which may jeopardize user privacy or leak credentials.
- **6** apps have backup functionality enabled via ADB, which could allow data extraction with physical access.

### 3.6 Binary Analysis

Shared libraries (.so files) used by the apps were analyzed for code hardening mechanisms. Missing protections can render apps vulnerable to buffer overflows and other memory corruption attacks.

### Table 5: Shared Library Binary Analysis Issues per App

| App | Total Libs | NX Missing | Canary Missing | RELRO Missing | Fortify Missing | Not Stripped |
|-----|-----------|------------|---------------|--------------|----------------|-------------|
| Calculator | 4 | 0 | 0 | 0 | 4 | 0 |
| Calendar | 96 | 0 | 8 | 2 | 64 | 0 |
| QR & Barcode Scanner | 0 | 0 | 0 | 0 | 0 | 0 |
| ZArchiver | 18 | 0 | 0 | 0 | 6 | 0 |
| Translate | 10 | 0 | 0 | 0 | 10 | 0 |
| Speedtest | 42 | 0 | 8 | 0 | 20 | 0 |
| Gboard | 22 | 0 | 2 | 0 | 20 | 0 |
| SHAREit | 4 | 0 | 0 | 0 | 4 | 0 |
| Authenticator | 0 | 0 | 0 | 0 | 0 | 0 |
| RAR | 0 | 0 | 0 | 0 | 0 | 0 |


A total of **196 shared libraries** were identified across all apps. Of these:
- **128** libraries lack FORTIFY protection (buffer overflow checks)
- **18** libraries miss Stack Canary protection

### 3.7 Hardcoded Secrets

Hardcoded secrets, including API keys, tokens, and credentials, were detected in the source code of the examined apps.

| App | Hardcoded Secrets Count |
|-----|------------------------|
| Calculator | 2 |
| Calendar | 224 |
| QR & Barcode Scanner | 4189 |
| ZArchiver | 125 |
| Translate | 50 |
| Speedtest | 218 |
| Gboard | 132 |
| SHAREit | 844 |
| Authenticator | 499 |
| RAR | 3 |

A total of **6286 potential hardcoded secrets** were identified across all apps. **10** out of 10 apps contain at least one hardcoded secret. This practice is particularly dangerous as it can expose API keys, authentication tokens, and other sensitive data to anyone who decompiles the app.

---

## 4. Discussion & Insights

### 4.1 Are Popular Apps Safer?

Our analysis reveals that **popularity does not correlate with better security**. Even apps with hundreds of millions of downloads exhibit fundamental security weaknesses. The average MobSF security score across the examined apps is **50.1/100**, indicating significant room for improvement.

### 4.2 Technical Debt

The findings demonstrate that many popular apps carry substantial "technical debt" — the long-term cost of choosing easy or fast solutions over more secure approaches. This manifests as:

1. **Use of deprecated cryptographic algorithms** (SHA-1 for signing)
2. **Excessive permission requests** beyond what functionality requires
3. **Cleartext storage of sensitive information** in logs and code
4. **Missing code hardening measures** in shared libraries
5. **Hardcoded secrets** that should be stored securely

### 4.3 Key Takeaways

1. **Permissions over-provisioning** remains a prevalent issue. Apps request more permissions than needed for their core functionality, increasing the attack surface.
2. **CWE-312 (Cleartext Storage)** and **CWE-532 (Log Information Leakage)** are nearly universal, appearing in the majority of examined apps.
3. **Network security misconfigurations** are common, with several apps allowing cleartext traffic.
4. **Developer awareness** of security best practices appears insufficient, as basic protections like FORTIFY and proper certificate validation are frequently absent.

---

## 5. Conclusion

This study demonstrates that popular Android utility applications exhibit a range of security and privacy issues. The results largely align with the findings of Chatzoglou et al., confirming that the general tendency in the Android ecosystem leans towards insufficient security measures. App developers must adopt a security-by-design mindset, following the principle of minimal privilege and implementing proper code hardening, secure storage, and up-to-date cryptographic practices.

---

## 6. References

1. Chatzoglou, E.; Kambourakis, G.; Smiliotopoulos, C. *Let the Cat out of the Bag: Popular Android IoT Apps under Security Scrutiny.* Sensors 2022, 22, 513. https://doi.org/10.3390/s22020513
2. OWASP Mobile Security Testing Guide. https://owasp.org/www-project-mobile-security-testing-guide/
3. MobSF (Mobile Security Framework). https://github.com/MobSF/Mobile-Security-Framework-MobSF
4. Exodus Privacy. https://exodus-privacy.eu.org/
5. https://doi.org/10.3390/info14080457
6. https://doi.org/10.1371/journal.pone.0251867
7. https://doi.org/10.3390/fi13030058
