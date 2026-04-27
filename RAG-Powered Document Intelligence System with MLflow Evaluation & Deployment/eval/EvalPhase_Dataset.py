EVAL_DATASET = [
    # ── PDF 01: Cancer Biology ────────────────────────────────────────────────
    {
        "id": "Q01",
        "question": "What are the hallmarks of cancer as described in cancer biology?",
        "expected_keywords": ["hallmarks", "cancer", "proliferation", "apoptosis", "angiogenesis"],
        "source_file": "01_cancer_biology_fundamentals.pdf",
    },
    {
        "id": "Q02",
        "question": "What role do CDK4/6 and cyclin D complexes play in the cell cycle?",
        "expected_keywords": ["CDK4", "cyclin D", "retinoblastoma", "Rb", "S-phase", "E2F"],
        "source_file": "01_cancer_biology_fundamentals.pdf",
    },

    # ── PDF 02: Staging ───────────────────────────────────────────────────────
    {
        "id": "Q03",
        "question": "What does the TNM staging system represent and what does each letter stand for?",
        "expected_keywords": ["TNM", "tumour", "node", "metastasis", "AJCC", "staging"],
        "source_file": "02_cancer_staging_classification.pdf",
    },
    {
        "id": "Q04",
        "question": "What is the difference between clinical staging and pathological staging?",
        "expected_keywords": ["clinical staging", "pathological staging", "cTNM", "pTNM", "surgical"],
        "source_file": "02_cancer_staging_classification.pdf",
    },

    # ── PDF 03: Chemotherapy ──────────────────────────────────────────────────
    {
        "id": "Q05",
        "question": "What is the log-kill hypothesis in chemotherapy and what does it imply for dosing?",
        "expected_keywords": ["log-kill", "first-order", "fraction", "combination", "dose"],
        "source_file": "03_chemotherapy_principles_regimens.pdf",
    },
    {
        "id": "Q06",
        "question": "What are the main classes of chemotherapy drugs and their mechanisms of action?",
        "expected_keywords": ["alkylating", "antimetabolites", "taxanes", "platinum", "DNA", "mechanism"],
        "source_file": "03_chemotherapy_principles_regimens.pdf",
    },

    # ── PDF 04: Targeted Therapy ──────────────────────────────────────────────
    {
        "id": "Q07",
        "question": "What is oncogene addiction and why is it relevant to targeted therapy?",
        "expected_keywords": ["oncogene addiction", "targeted", "molecular", "dependency", "TKI"],
        "source_file": "04_targeted_therapy_precision_oncology.pdf",
    },
    {
        "id": "Q08",
        "question": "What is a companion diagnostic and what role does it play in precision oncology?",
        "expected_keywords": ["companion diagnostic", "CDx", "biomarker", "FDA", "alteration"],
        "source_file": "04_targeted_therapy_precision_oncology.pdf",
    },

    # ── PDF 05: Immuno-Oncology ───────────────────────────────────────────────
    {
        "id": "Q09",
        "question": "What is the difference between PD-1 and CTLA-4 immune checkpoints?",
        "expected_keywords": ["PD-1", "CTLA-4", "T-cell", "checkpoint", "tumour microenvironment", "lymph node"],
        "source_file": "05_immuno_oncology_checkpoint_inhibitors.pdf",
    },
    {
        "id": "Q10",
        "question": "What are immune-related adverse events (irAEs) and how are they managed?",
        "expected_keywords": ["irAE", "immune-related", "adverse", "corticosteroid", "colitis", "pneumonitis"],
        "source_file": "05_immuno_oncology_checkpoint_inhibitors.pdf",
    },

    # ── PDF 06: Radiation Oncology ────────────────────────────────────────────
    {
        "id": "Q11",
        "question": "What are the 5 R's of radiobiology and what is the clinical significance of each?",
        "expected_keywords": ["repair", "redistribution", "repopulation", "reoxygenation", "radiosensitivity", "fractionation"],
        "source_file": "06_radiation_oncology_fundamentals.pdf",
    },

    # ── PDF 07: Breast Cancer ─────────────────────────────────────────────────
    {
        "id": "Q12",
        "question": "What are the molecular subtypes of breast cancer and how do they differ in treatment?",
        "expected_keywords": ["ER", "HER2", "TNBC", "luminal", "subtype", "Ki-67"],
        "source_file": "07_breast_cancer_diagnosis_treatment.pdf",
    },

    # ── PDF 08: Lung Cancer ───────────────────────────────────────────────────
    {
        "id": "Q13",
        "question": "Which molecular alterations are actionable in non-small cell lung cancer (NSCLC)?",
        "expected_keywords": ["EGFR", "ALK", "ROS1", "MET", "KRAS", "NSCLC", "TKI"],
        "source_file": "08_lung_cancer_nsclc_sclc.pdf",
    },

    # ── PDF 09: Colorectal Cancer ─────────────────────────────────────────────
    {
        "id": "Q14",
        "question": "What colorectal cancer screening modalities are recommended and at what intervals?",
        "expected_keywords": ["screening", "colonoscopy", "FIT", "stool", "interval", "colorectal"],
        "source_file": "09_colorectal_cancer_management.pdf",
    },

    # ── PDF 10: Haematological Malignancies ───────────────────────────────────
    {
        "id": "Q15",
        "question": "What is the standard treatment approach for diffuse large B-cell lymphoma (DLBCL)?",
        "expected_keywords": ["DLBCL", "R-CHOP", "rituximab", "lymphoma", "B-cell", "NHL"],
        "source_file": "10_haematological_malignancies.pdf",
    },

    # ── PDF 11: Cancer Genetics ───────────────────────────────────────────────
    {
        "id": "Q16",
        "question": "What percentage of cancers arise from hereditary predisposition and what are the key syndromes?",
        "expected_keywords": ["hereditary", "BRCA", "Lynch syndrome", "germline", "5-10%", "predisposition"],
        "source_file": "11_cancer_genetics_hereditary_syndromes.pdf",
    },

    # ── PDF 12: Palliative Care ───────────────────────────────────────────────
    {
        "id": "Q17",
        "question": "What is the WHO cancer pain ladder and how is it applied in clinical practice?",
        "expected_keywords": ["WHO", "pain ladder", "opioid", "step", "analgesic", "morphine"],
        "source_file": "12_palliative_care_symptom_management.pdf",
    },

    # ── PDF 13: Surgical Oncology ─────────────────────────────────────────────
    {
        "id": "Q18",
        "question": "What is the purpose of sentinel lymph node biopsy and when is it indicated?",
        "expected_keywords": ["sentinel lymph node", "SLN", "biopsy", "mapping", "axillary", "staging"],
        "source_file": "13_surgical_oncology_principles.pdf",
    },

    # ── PDF 14: Oncological Emergencies ──────────────────────────────────────
    {
        "id": "Q19",
        "question": "How is febrile neutropenia defined and what is the initial management approach?",
        "expected_keywords": ["febrile neutropenia", "ANC", "temperature", "MASCC", "antibiotic", "ciprofloxacin"],
        "source_file": "14_oncological_emergencies.pdf",
    },

    # ── PDF 15: Clinical Trials ───────────────────────────────────────────────
    {
        "id": "Q20",
        "question": "What are the phases of clinical trials and what is the primary objective of each phase?",
        "expected_keywords": ["Phase I", "Phase II", "Phase III", "MTD", "efficacy", "randomised"],
        "source_file": "15_clinical_trials_evidence_based_oncology.pdf",
    },
]
