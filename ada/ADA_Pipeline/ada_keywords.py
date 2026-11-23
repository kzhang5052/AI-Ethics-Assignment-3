"""Draft retrieval rules adapted from the TA's ADA template.

L4: Real-time scam pattern flagging tuned for seniors (e.g., impostor,
lottery, tech-support) — Policy (docs), ADA.

These rules find candidate passages, not proof of compliance. Pass a sentence
or paragraph to topic_tags(). Review context, product scope, and evidence type.
This module is standalone; the TA's downstream coercion-specific analysis
must also be adapted before using these topics in that pipeline.
"""

import re


TOPICS = {
    "scam patterns": re.compile(
        r"\bscam\w*|\bfraud\w*|\bimpost[eo]r\w*|\bimpersonat\w*"
        r"|\bphishing\b|\bsweepstakes?\b|\blotter(?:y|ies)\b"
        r"|\b(?:tech(?:nical)?[- ]support|advance[- ]fee|prize)\s+scams?\b",
        re.I,
    ),
    "flagging/warnings": re.compile(
        r"\bdetect\w*|\bidentif\w*|\bflag(?:s|ged|ging)?\b"
        r"|\balert\w*|\bwarn\w*|\brecogni[sz]\w*"
        r"|\bsuspicious\s+(?:messages?|calls?|links?|activity|transactions?)\b"
        r"|\bscam\s+(?:signals?|indicators?)\b",
        re.I,
    ),
    "seniors": re.compile(
        r"\bseniors?\b|\bolder\s+(?:adults?|people|persons?|users?|customers?)\b"
        r"|\belderly\b|\belders?\b|\belder[- ]targeted\b"
        r"|\bage(?:d|s)?\s+65\s*(?:\+|and\s+(?:older|over|above))",
        re.I,
    ),
    "tailoring": re.compile(
        r"\btailor\w*|\badapt\w*|\btun(?:e|ed|es|ing)\b"
        r"|\bage[- ](?:specific|appropriate|sensitive)\b"
        r"|\baccessib\w*|\bplain[- ]language\b"
        r"|\beasy[- ]to[- ]understand\b|\b(?:cognitive|digital)\s+literacy\b"
        r"|\bdesigned\s+for\b",
        re.I,
    ),
    "during-interaction protection": re.compile(
        r"\breal[- ]time\b|\brun[- ]?time\b"
        r"|\bduring\s+(?:the\s+|an?\s+)?(?:conversation|interaction|call|chat)\b"
        r"|\bincoming\s+(?:messages?|calls?|texts?)\b"
        r"|\b(?:immediate|instant|live)\s+(?:warnings?|alerts?|detection)\b"
        r"|\bbefore\s+(?:sending|paying|transferring|clicking)\b",
        re.I,
    ),
}

# Provisional quotation-ranking weights, NOT safety or compliance scores.
TOPIC_WEIGHT = {
    "scam patterns": 3,
    "flagging/warnings": 3,
    "seniors": 3,
    "tailoring": 2,
    "during-interaction protection": 1,
}

# Like the TA's THREAT_NOISE, remove obvious false matches before tagging.
# Apply each filter ONLY to its own topic, preserving other relevant evidence.
# Do not discard an entire sentence simply because it contains a noise phrase.
TOPIC_NOISE = {
    "seniors": re.compile(
        r"\bsenior\s+(?:software\s+)?(?:engineers?|developers?|managers?|"
        r"management|executives?|officials?|analysts?|researchers?|leadership)\b"
        r"|\b(?:high[- ]school|college)\s+seniors?\b",
        re.I,
    ),
    "flagging/warnings": re.compile(
        r"\bcommand[- ]line\s+flags?\b|\bfeature\s+flags?\b"
        r"|\bwarning\s+(?:messages?\s+)?(?:from\s+the\s+)?compiler\b"
        r"|\bcompiler\s+warnings?\b",
        re.I,
    ),
    "during-interaction protection": re.compile(
        r"\brun[- ]?time\s+(?:errors?|exceptions?|environments?|libraries|"
        r"dependencies|versions?)\b",
        re.I,
    ),
}


def topic_tags(text):
    """Return topic matches; keep the original text unchanged for quotation."""
    tags = []
    for name, pattern in TOPICS.items():
        noise = TOPIC_NOISE.get(name)
        cleaned = noise.sub(" ", text) if noise else text
        if pattern.search(cleaned):
            tags.append(name)
    return tags


# Review rules:
# - Scam + warning language is a candidate, not necessarily a model policy.
# - "Seniors" and "tailoring" must be related in context to support tuning.
# - Age 65 is a retrieval example, not a project definition of "senior".
# - A legitimate lottery can match; inspect context before labeling it a scam.
# - "Contact tech support" alone is not a tech-support scam pattern.
# - User fraud prohibitions remain user_restriction evidence, not noise.
# - Missing keywords mean no rule match, not absence of a protective policy.
