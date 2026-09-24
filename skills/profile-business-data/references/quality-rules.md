# Quality rules
Required: feedback_id, product_name, feedback_text, rating, channel, submission_date, region.
- rating must be numeric 1 to 5
- submission_date must parse as a date
- feedback_id must be nonblank and unique
- blank feedback_text is rejected
- exact duplicate rows are flagged
- unknown categories are warnings, not automatic deletions
