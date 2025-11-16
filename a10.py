"""
Sample application with deliberate code quality and security issues
This demonstrates how linting tools detect problems
"""

import os
import sys
import unused_module  # Issue: Unused import

# Issue: Line too long (PEP 8 recommends max 79 characters)
def calculate_user_discount(user_age, user_membership_level, purchase_amount, has_coupon, is_premium_member):
    """Calculate discount with poor code quality"""
    
    # Issue: Multiple statements on one line
    x=5; y=10; z=x+y
    
    # Issue: Undefined variable
    result = undefined_variable + 10
    
    # Issue: Potential SQL injection vulnerability
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM users WHERE id = " + user_id  # Dangerous!
    
    # Issue: Using eval() - major security risk
    user_input = input("Enter calculation: ")
    result = eval(user_input)  # Very dangerous!
    
    # Issue: Bare except clause (catches everything)
    try:
        risky_operation()
    except:  # Should specify exception type
        pass
    
    # Issue: Comparison to None should use 'is'
    if user_age == None:
        return 0
    
    # Issue: Unused variable
    unused_var = "This is never used"
    
    # Issue: Missing whitespace around operator
    discount=0.1
    
    # Issue: Line with only whitespace (trailing spaces)
    
    
    # Issue: Multiple blank lines (PEP 8 recommends max 2)
    
    
    
    
    return discount


def process_password(password):
    """Poor password handling - security issue"""
    
    # Issue: Hardcoded password (security vulnerability)
    admin_password = "admin123"
    
    # Issue: Using MD5 for passwords (insecure hash)
    import hashlib
    hashed = hashlib.md5(password.encode()).hexdigest()
    
    # Issue: Printing sensitive data
    print(f"User password: {password}")
    
    return hashed


def read_file(filename):
    """Unsafe file operations"""
    
    # Issue: Path traversal vulnerability (no validation)
    with open(filename, 'r') as f:
        content = f.read()
    
    return content


# Issue: Code not protected by if __name__ == "__main__"
calculate_user_discount(25, "gold", 100, True, True)
process_password("secret123")
read_file("/etc/passwd")
