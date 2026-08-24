from actuated_minds_crm.models import Contact, AuditIssue, IssueType, Severity


class CRMAuditor:

    def check_missing_fields(self, contact: Contact) -> list:
        issues = []
        if not(contact.has_linkedin() == True):
            issues.append(AuditIssue(
                contact_name=contact.name,
                field="linkedin",
                issue_type=IssueType.MISSING_FIELD,
                severity=Severity.WARNING
                ))

        issues.append(AuditIssue(
                                contact_name=contact.name,
                                field="role",
                                issue_type=IssueType.MISSING_FIELD,
                                severity=Severity.WARNING
                                ))

        issues.append(AuditIssue(
                                contact_name=contact.name,
                                field="organisation",
                                issue_type=IssueType.MISSING_FIELD,
                                severity=Severity.WARNING
                                ))

        issues.append(AuditIssue(
                                contact_name=contact.name,
                                field="region",
                                issue_type=IssueType.MISSING_FIELD,
                                severity=Severity.WARNING
                                ))

        issues.append(AuditIssue(
                                contact_name=contact.name,
                                field="source_url",
                                issue_type=IssueType.MISSING_FIELD,
                                severity=Severity.WARNING
                                ))

        return issues

    def check_linkedin(self, contact: Contact):
        issues = []
        if (contact.has_linkedin() == True) and (contact.has_valid_linkedin_format() == False):
                    issues.append(AuditIssue(
                        contact_name=contact.name,
                        field="linkedin",
                        issue_type=IssueType.MALFORMED_LINKEDIN,
                        severity=Severity.ERROR
                        ))
        return issues

    def audit_contact(self, contact: Contact):
        issues = []
        issues.extend(self.check_missing_fields(contact))
        issues.extend(self.check_linkedin(contact))
        return issues