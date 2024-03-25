using System;
using System.Collections.Generic;
using System.Linq;
using Xunit;

namespace SimpleUnitTests.Tests
{
    // Do not change the name of this class
    public class PasswordValidatorUnitTests
    {
        // Do not change.
        // This is your SUT (System Under Test) which should be used in tests.
        // It is not null but it is not initialized i.e. Initialize method was not called.
        public IPasswordValidator ValidatorToTest { get; set; }

        // All your test methods should be public, have no parameters and be marked with [CustomFact] attribute
        [CustomFact]
        public void SampleTest()
        {
            ValidatorToTest.Initialize(10, 45, true, false);
            var res = ValidatorToTest.Validate("ABCabcd123");
            Assert.True(res.Errors.Getlength()==0);

            // TODO - Assertions
            Console.WriteLine("Sample debug output");
        }
    }
}

/*
public interface IPasswordValidator
{
    /// <summary>
    /// Initialize a password validator.
    /// </summary>
    ///
    /// <param name="minLength">The minimum length of the passowrd</param>
    /// <param name="maxLength">The maximum length of the passowrd</param>
    /// <param name="mustContainDigits"><c>true</c> - a password must contain at least 1 digit</param>
    /// <param name="mustContainCapitalLetters"><c>true</c> - a password must contain at least 1 capital letter</param>
    ///
    /// <exception cref="IndexOutOfRangeException">If minLength is lower than or equal to zero</exception>
    /// <exception cref="IndexOutOfRangeException">If maxLength is greater than 255</exception>
    /// <exception cref="ArgumentException">If minLength is greater than maxLength</exception>
    void Initialize(
        int minLength,
        int maxLength,
        bool mustContainDigits,
        bool mustContainCapitalLetters);

    /// <summary>
    /// Validates a provided password
    /// </summary>
    /// <param name="password">A password to validate</param>
    /// <returns>A validator result</returns>
    ValidationResult Validate(string password);
}
*/

/*
public class ValidationResult
{
    /// <summary>
    /// Returns <c>true</c> only if a password matches all the rules
    /// </summary>
    public bool IsCorrect { get; set; }

    /// <summary>
    /// If <c>IsCorrect</c> is <c>true</c> then this property returns an empty arrray.
    /// Otherwise it returns all found errors. Errors cannot be duplicated.
    /// This property must not be null.
    /// </summary>
    public ValidationErrorEnum[] Errors { get; set; }
}
*/

/*
public enum ValidationErrorEnum
{
    IsEmpty, // If a password is an empty string or null
    IsTooShort, // If the length of a password is < minLength
    IsTooLong, // If the length of a password is > maxLength
    DoesNotContainDigits,
    DoesNotContainCapitalLetters
}
*/

/*
Assert.Throws<Exception>(() => ... );
Assert.True(value);
Assert.False(value);
Assert.Equal(expected, actual);
Assert.NotEqual(expected, actual);
*/
