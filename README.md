# Hospital & Patient Management System (HMS) - Frappe v16

A comprehensive Hospital ERP system built for Frappe / ERPNext v16.

## Features & Modules

1. **Hospital Setup**: Multi-branch hospitals, clinical departments, medical specialties, rooms, wards, beds, doctor/staff profiles.
2. **Patient Management**: Centralized patient master, MRN auto-generation, contact info, medical history, allergy tracking.
3. **Appointment Management**: Doctor schedule, slot allocation, appointments workflow (`Scheduled` -> `Checked In` -> `In Consultation` -> `Completed`).
4. **Clinical Records (OPD)**: Patient encounters, vitals recording with BMI calculation, diagnosis master, medication master, drug prescriptions.
5. **IPD / Inpatient Management**: Admission tracking, bed allocation, bed status updates, discharge summary.
6. **Nursing Management**: Shift notes, Medication Administration Record (MAR).
7. **Laboratory**: Test masters, lab order requisitions, lab results entry with abnormal flagging.
8. **Radiology**: Imaging orders (X-Ray, CT, MRI, USG), radiology reports.
9. **Pharmacy Dispensing**: Prescriptions processing and inventory linkage.
10. **Billing & Insurance**: Patient invoices (service charges, bed stay, lab, pharmacy), insurance claim tracking.
11. **Dashboards & Workspaces**: Dedicated Hospital Management Workspace for quick access and clinical metrics.

## Installation

```bash
bench get-app https://github.com/sagarmemane135/HMS.git --branch main
bench --site [site-name] install-app hms
bench --site [site-name] migrate
```

## License

MIT
