JURISDICTION_DATA = {
    "lagos": {
        "name": "Lagos State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Pre-Action Protocol mandatory. Order 57 (Small Claims) applies.",
        "courts": "Ikeja, Lagos Island, Ikorodu, Epe, Badagry",
        "compliance": "Section 84 Evidence Act for JIS printouts.",
        "color": "success"
    },
    "abuja": {
        "name": "Abuja (FCT)",
        "limit": "₦5,000,000",
        "timeline": "12 Months",
        "rules": "2025 E-Filing Rules apply. High Court Civil Procedure Rules 2018.",
        "courts": "Maitama, Garki, Wuse, Nyanya",
        "compliance": "Electronic filing receipt mandatory for Section 84.",
        "color": "primary"
    },
    "kwara": {
        "name": "Kwara State",
        "limit": "₦3,000,000",
        "timeline": "60 Days",
        "rules": "Gateway ADR focus. Magistrate Court Small Claims Procedure 2023.",
        "courts": "Ilorin, Offa, Omu-Aran",
        "compliance": "ADR certificate must precede Section 84 certification.",
        "color": "info"
    },
    "kano": {
        "name": "Kano State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Northern Trade rules. Sharia and Common Law dual-pathway consideration.",
        "courts": "Kano City, Gwale, Fagge",
        "compliance": "Certified True Copy (CTC) requirements for digital logs.",
        "color": "danger"
    },
    "oyo": {
        "name": "Oyo State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Pace Setter protocols. 2022 Small Claims Directions.",
        "courts": "Ibadan, Oyo, Ogbomoso",
        "compliance": "Verification of affidavit for all digital evidence.",
        "color": "warning"
    },
    "enugu": {
        "name": "Enugu State",
        "limit": "₦5,000,000",
        "timeline": "30 Days",
        "rules": "High-automation e-portal. Rapid trial track for debt recovery.",
        "courts": "Enugu, Nsukka, Agbani",
        "compliance": "E-portal metadata required for authentication.",
        "color": "dark"
    },
    "abia": {
        "name": "Abia State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Fast-track registry. 2024 Practice Directions on liquidated money demands.",
        "courts": "Umuahia, Aba, Ohafia",
        "compliance": "Registry stamp required on digital printouts.",
        "color": "primary"
    },
    "osun": {
        "name": "Osun State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Multi-door courthouse first. Small Claims District 2023.",
        "courts": "Osogbo, Ife, Ilesa",
        "compliance": "ADR settlement attempts must be logged in system.",
        "color": "info"
    },
    "ogun": {
        "name": "Ogun State",
        "limit": "₦500,000",
        "timeline": "60 Days",
        "rules": "Customary Court of Appeal focus. Strict focus on localized recovery.",
        "courts": "Abeokuta, Ijebu-Ode, Sagamu",
        "compliance": "Traditional witness testimony logs required.",
        "color": "success"
    },
    "ekiti": {
        "name": "Ekiti State",
        "limit": "₦5,000,000",
        "timeline": "30 Days",
        "rules": "Practice Direction 2020/25. Rapid Small Claims activation.",
        "courts": "Ado-Ekiti, Ikere, Ijero",
        "compliance": "Service of process via WhatsApp/Email permitted.",
        "color": "warning"
    },
    "ondo": {
        "name": "Ondo State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Sunshine State legal codes. Revised Magistrate Rules 2024.",
        "courts": "Akure, Ondo, Owo",
        "compliance": "Digital case log must match physical register.",
        "color": "danger"
    },
    "river": {
        "name": "Rivers State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Admiralty/Energy focus. High Court (Small Claims) Rules 2023.",
        "courts": "Port Harcourt, Obio/Akpor, Eleme",
        "compliance": "Technical expert affidavits for energy-related claims.",
        "color": "secondary"
    },
    "anambra": {
        "name": "Anambra State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Land recovery focus. 2024 Magistrate Court (Civil Procedure) Rules.",
        "courts": "Awka, Onitsha, Nnewi",
        "compliance": "Survey plan digital authentication required.",
        "color": "success"
    },
    "kaduna": {
        "name": "Kaduna State",
        "limit": "₦3,000,000",
        "timeline": "60 Days",
        "rules": "Mediation-first logic. Small Claims Court Handbook 2023.",
        "courts": "Kaduna, Zaria, Kafanchan",
        "compliance": "Mediation outcome report linked to Section 84.",
        "color": "primary"
    },
    "edo": {
        "name": "Edo State",
        "limit": "₦5,000,000",
        "timeline": "60 Days",
        "rules": "Magisterial District rules. High Court Civil Procedure (Amendment) 2023.",
        "courts": "Benin City, Ekpoma, Auchi",
        "compliance": "Video evidence protocols under Section 84(2).",
        "color": "dark"
    }
}

def get_state_rules(state_key):
    return JURISDICTION_DATA.get(state_key.lower(), {})