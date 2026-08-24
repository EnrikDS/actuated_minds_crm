from pydantic import BaseModel
from datetime import datetime
from enum import Enum


class Severity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"

class IssueType(str, Enum):
    MISSING_FIELD = "missing_field"
    MALFORMED_LINKEDIN = "malformed_linkedin"
    WHITESPACE = "whitespace"
    DUPLICATE = "duplicate"
    OVERDUE_FOLLOWUP = "overdue_followup"

class Contact(BaseModel):
        name: str
        priority: str | None = None
        region: str | None = None
        organisation: str 
        category: str | None = None
        relevant_themes: str | None = None
        typical_stage: str | None = None
        why_this_contact: str | None = None
        website: str | None = None
        best_buyer_persona: str | None = None
        role: str | None = None
        linkedin_url: str = None 
        connection_sent: bool = None
        innconectable: bool = None
        longer_message_sent: bool = None
        confidence: str = None
        source_url: str = None
        outreach_angle: str | None = None
        last_contacted: datetime | None = None
        next_follow_up: datetime | None = None
        outcome: str = None

        def has_linkedin(self) -> bool:
            return self.linkedin_url is not None and self.linkedin_url.strip() != ""

        def has_valid_linkedin_format(self) -> bool:
            if not self.has_linkedin():
                return False
            linkedin_url = self.linkedin_url.strip()
            return linkedin_url.startswith("https://www.linkedin.com/in/") or linkedin_url.startswith("https://linkedin.com/in/")

        def is_follow_up_due(self) -> bool:
            if self.next_follow_up is None:
                return False
            return datetime.now() >= self.next_follow_up

        def get_whitespace_fields() -> list:
            whitespace_fields = []
            for field_name, value in self.__dict__.items():
                if isinstance(value, str) and value.strip() == "":
                    whitespace_fields.append(field_name)
            return whitespace_fields

class AuditIssue(BaseModel):
    contact_name: str
    field: str
    issue_type : IssueType
    severity: Severity
    current_value: str |None
    message: str

