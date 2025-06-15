"""Intent validation — ensures intents are well-formed and economically viable."""
from dataclasses import dataclass

@dataclass
class ValidationReport:
    valid: bool
    errors: list[str]
    warnings: list[str]
    estimated_gas: int
    estimated_fee: int

class IntentValidator:
    MIN_REWARD = 1000
    MAX_AMOUNT = 10**30
    MIN_AMOUNT = 10**12
    
    def validate(self, intent) -> ValidationReport:
        errors = []
        warnings = []
        
        if intent.amount_in < self.MIN_AMOUNT:
            errors.append("Amount too small")
        if intent.amount_in > self.MAX_AMOUNT:
            errors.append("Amount too large")
        if intent.reward < self.MIN_REWARD:
            warnings.append(f"Low reward: {intent.reward}, min recommended: {self.MIN_REWARD}")
        if intent.min_amount_out <= 0:
            errors.append("Min output must be > 0")
            
        return ValidationReport(
            valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            estimated_gas=150000,
            estimated_fee=intent.reward // 100
        )
