# Βγάζοντας τη γάτα από τον σάκο: Δημοφιλείς Android Εφαρμογές υπό το Πρίσμα της Ασφάλειας

## 1. Περίληψη (Abstract)

Η παρούσα αναφορά παρουσιάζει μια ολοκληρωμένη αξιολόγηση ασφαλείας **12 δημοφιλών εφαρμογών Android**. Ακολουθώντας τη μεθοδολογία των Chatzoglou et al. στο άρθρο "Let the Cat out of the Bag: Popular Android IoT Apps under Security Scrutiny", πραγματοποιούμε στατική ανάλυση χρησιμοποιώντας το Mobile Security Framework (MobSF). Η ανάλυσή μας εκτείνεται σε πολλούς άξονες, συμπεριλαμβανομένων των ευαίσθητων δικαιωμάτων (permissions), των αδυναμιών κώδικα (CWEs), των σφαλμάτων διαμόρφωσης ασφάλειας δικτύου, των ευπαθειών στο manifest, των ενσωματωμένων μυστικών, της χρήσης trackers (ιχνηλατών) και της ανάλυσης δυαδικών αρχείων των κοινόχρηστων βιβλιοθηκών.

Τα αποτελέσματα αποκαλύπτουν ότι ακόμη και ευρέως χρησιμοποιούμενες εφαρμογές εμφανίζουν σημαντικά κενά ασφάλειας και προστασίας προσωπικών δεδομένων.

---

## 2. Μεθοδολογία (Methodology)

Επιλέξαμε 12 δημοφιλείς εφαρμογές για ανάλυση. Το περιβάλλον ανάλυσης βασίστηκε στο Mobile Security Framework (MobSF) για την αυτοματοποιημένη στατική ανάλυση των αρχείων APK.

---

## 3. Αποτελέσματα (Results)

### 3.1 Επισκόπηση Εφαρμογών
### Πίνακας 1: Επισκόπηση Εξεταζόμενων Εφαρμογών Android

| Α/Α | Όνομα Εφαρμογής | Όνομα Πακέτου | Έκδοση | Μέγεθος | Λήψεις | Βαθμολογία |
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
| 11 | CCleaner | `com.piriform.ccleaner` | 26.03.0 | 46.58MB | 100,000,000+ | 4.6 |
| 12 | Turbo VPN | `free.vpn.unblock.proxy.turbovpn` | 4.2.9.7 | 52.97MB | 100,000,000+ | 4.7 |


### 3.2 Στατική Ανάλυση Υψηλού Επιπέδου: Δικαιώματα (Permissions)
Αναγνώριση των επικίνδυνων δικαιωμάτων.
### Πίνακας 2: Εντοπισμένα Επικίνδυνα Δικαιώματα (Permissions) ανά Εφαρμογή

| Εφαρμογή | U1 | U2 | A1 | A2 | A3 | A4 | L1 | L2 | L3 | L4 | S1 | S2 | S3 | P1 | P2 | P3 | P6 | P7 | P9 | P10 | Σύνολο |
|-----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|-------|
| Calculator |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | ✓ |  |  | **1** |
| Calendar |  |  |  |  |  |  | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |  | ✓ | ✓ |  | ✓ | ✓ | **9** |
| QR & Barcode Scanner | ✓ |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  |  | **3** |
| ZArchiver |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |  |  |  | **3** |
| Translate |  | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |  | ✓ |  |  |  |  |  | **3** |
| Speedtest | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ |  | ✓ |  |  |  |  |  |  | **7** |
| Gboard | ✓ | ✓ |  |  | ✓ |  |  |  |  |  | ✓ |  |  |  |  | ✓ |  |  |  |  | **5** |
| SHAREit | ✓ |  |  |  |  |  | ✓ | ✓ |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ |  | **10** |
| Authenticator | ✓ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | **1** |
| RAR |  |  |  |  |  |  |  |  |  |  |  | ✓ | ✓ |  |  |  |  |  |  |  | **2** |
| CCleaner |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ | ✓ |  | ✓ |  |  | ✓ |  |  |  | **10** |
| Turbo VPN | ✓ |  |  |  |  |  |  |  |  |  | ✓ |  |  |  |  |  |  |  |  |  | **2** |
| **ΣΥΝΟΛΟ** | 6 | 2 | 1 | 1 | 2 | 1 | 4 | 4 | 1 | 1 | 8 | 8 | 3 | 2 | 2 | 3 | 3 | 1 | 2 | 1 | |

**Υπόμνημα Δικαιωμάτων:**
- **U1**: CAMERA (Κάμερα)
- **U2**: RECORD_AUDIO (Ήχος)
- **A1**: USE_CREDENTIALS
- **A2**: AUTHENTICATE_ACCOUNTS
- **A3**: GET_ACCOUNTS
- **A4**: MANAGE_ACCOUNTS
- **L1**: ACCESS_FINE_LOCATION (Ακριβής Τοποθεσία)
- **L2**: ACCESS_COARSE_LOCATION
- **L3**: ACCESS_BACKGROUND_LOCATION
- **L4**: ACCESS_MEDIA_LOCATION
- **S1**: READ_EXTERNAL_STORAGE (Ανάγνωση Αποθ.)
- **S2**: WRITE_EXTERNAL_STORAGE (Εγγραφή Αποθ.)
- **S3**: REQUEST_INSTALL_PACKAGES
- **P1**: READ_PHONE_STATE
- **P2**: SYSTEM_ALERT_WINDOW
- **P3**: READ_CONTACTS
- **P6**: WRITE_SETTINGS
- **P7**: GET_TASKS
- **P9**: READ_CALENDAR
- **P10**: WRITE_CALENDAR

### 3.3 Στατική Ανάλυση Χαμηλού Επιπέδου: Αδυναμίες Κώδικα (CWEs)
Βαθύτερη ανάλυση για ευπάθειες Janus, διαμόρφωση δικτύου και αδυναμίες కώδικα.
### Πίνακας 3: Εντοπισμένες Αδυναμίες και Θέματα Ασφάλειας ανά Εφαρμογή

| Εφαρμογή | Janus | Ασφάλεια Δικτ. | APK Υπογρ. | CWE-89 | CWE-250 | CWE-276 | CWE-295 | CWE-312 | CWE-327 | CWE-330 | CWE-532 | CWE-649 | CWE-749 | CWE-919 | Μυστικά | Βαθμ. |
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
| CCleaner |  |  | SHA512 | ✓ |  | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 4303 | 46 |
| Turbo VPN | ✓ |  | SHA512 | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | 273 | 45 |

**Σύμβολα Ασφάλειας Δικτύου:** ● = απλό κείμενο (cleartext) σε όλους τους τομείς, ◎ = απλό κείμενο σε συγκεκριμένους τομείς, ⊠ = εμπιστεύεται πιστοποιητικά συστήματος, ⊞ = εμπιστεύεται πιστοποιητικά χρήστη, ⊡ = παρακάμπτει το certificate pinning

### 3.4 Ανάλυση Tracker (Tracker Analysis)
### Πίνακας 6: Εντοπισμένοι Ιχνηλάτες (Trackers) ανά Εφαρμογή

| Εφαρμογή | Πλήθος Trackers | Ονόματα Trackers |
|-----|---------------|---------------|
| Calculator | 0 |  |
| Calendar | 0 |  |
| QR & Barcode Scanner | 3 | Facebook Ads, Google AdMob, Google Firebase Analytics |
| ZArchiver | 0 |  |
| Translate | 0 |  |
| Speedtest | 10 | Amazon Advertisement, Amazon Mobile Analytics (Amplify), ComScore, Google AdMob, Google Analytics (+5 ακόμα) |
| Gboard | 0 |  |
| SHAREit | 14 | Adjust, AppMonet, Facebook Analytics, Facebook Login, Google AdMob (+9 ακόμα) |
| Authenticator | 0 |  |
| RAR | 0 |  |
| CCleaner | 10 | AppLovin (MAX and SparkLabs), Facebook Ads, Google AdMob, Google CrashLytics, Google Firebase Analytics (+5 ακόμα) |
| Turbo VPN | 11 | Adjust, AppMonet, ChartBoost, Google AdMob, Google CrashLytics (+6 ακόμα) |


### 3.5 Ανάλυση Manifest (Manifest Analysis)
### Πίνακας 4: Αποτελέσματα Ανάλυσης Manifest ανά Εφαρμογή

| Εφαρμογή | Εξαγ. Δραστ. | Εξαγ. Υπηρ. | Εξαγ. Δέκτες | Εξαγ. Πάροχοι | Cleartext | Backup | Αποσφαλμ. | Υψηλ. Κινδ. | Προειδοπ. |
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
| CCleaner | 10 | 7 | 8 | 0 |  |  |  | 0 | 26 |
| Turbo VPN | 2 | 2 | 4 | 1 |  |  |  | 1 | 9 |


### 3.6 Ανάλυση Δυαδικών Αρχείων (Binary Analysis)
### Πίνακας 5: Θέματα Ασφάλειας Δυαδικών Αρχείων (Shared Libraries)

| Εφαρμογή | Σύνολο Libs | Απουσία NX | Απουσία Canary | Απουσία RELRO | Απουσία Fortify | Όχι Stripped |
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
| CCleaner | 0 | 0 | 0 | 0 | 0 | 0 |
| Turbo VPN | 0 | 0 | 0 | 0 | 0 | 0 |

### 3.7 Ενσωματωμένα Μυστικά (Hardcoded Secrets)
Εντοπίστηκαν 10862 συνολικά ενσωματωμένα μυστικά σε όλες τις εφαρμογές.

---

## 4. Συζήτηση & Συμπεράσματα (Discussion & Insights)
Η ανάλυση επιβεβαιώνει ότι οι δημοφιλείς εφαρμογές δεν είναι απαραίτητα πιο ασφαλείς. Τα περιστατικά υπερχρήσης δικαιωμάτων επισκιάζουν τις πραγματικές ανάγκες της εφαρμογής, ενώ η αποθήκευση δεδομένων σε απλό κείμενο παραμένει ένα συχνό φαινόμενο.

---

## 5. Τελικό Συμπέρασμα (Conclusion)
Οι σύγχρονες εφαρμογές Android συχνά θυσιάζουν την ασφάλεια (security by design) και την προστασία των προσωπικών δεδομένων (privacy by design) προς χάριν της λειτουργικότητας.

---

## 6. Βιβλιογραφία (References)
1. Chatzoglou, E.; Kambourakis, G.; Smiliotopoulos, C. *Let the Cat out of the Bag: Popular Android IoT Apps under Security Scrutiny.* Sensors 2022, 22, 513. https://doi.org/10.3390/s22020513
2. OWASP Mobile Security Testing Guide.
3. MobSF (Mobile Security Framework).
4. Exodus Privacy.
