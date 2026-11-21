---
catalog: module
lean: CompPoly.GuruswamiSudan.shiftPolynomialByXPower, CompPoly.GuruswamiSudan.shiftedSubstitutionCoeffTerm, CompPoly.GuruswamiSudan.substituteYPolynomialPlusXPowerY, CompPoly.GuruswamiSudan.substituteYPolynomialPlusXPowerYTruncated
statement: formalized
proof: formalized
---

# Shifted Substitution for Guruswami-Sudan Root Search

`CompPoly.Bivariate.GuruswamiSudan.Root.ShiftedSubstitution`, in [CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean), by Valerii Huhnin.

> Executable substitution of `Y = f(X) + X^t Y` in bivariate polynomials.

`CompPoly.GuruswamiSudan.shiftPolynomialByXPower` (definition, [line 23](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean#L23))

> Multiply a univariate polynomial by `X^t`.

```lean
def shiftPolynomialByXPower {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (p : CPolynomial F) (t : Nat) : CPolynomial F
```

`CompPoly.GuruswamiSudan.shiftedSubstitutionCoeffTerm` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean#L30))

> The contribution of one `Y^y` coefficient to `Y^r` after substituting
> `Y = f(X) + X^t Y`.

```lean
def shiftedSubstitutionCoeffTerm {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (coeffY f : CPolynomial F) (t y r : Nat) : CPolynomial F
```

`CompPoly.GuruswamiSudan.substituteYPolynomialPlusXPowerY` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean#L37))

> Substitute `Y = f(X) + X^t Y` into a bivariate polynomial.

```lean
def substituteYPolynomialPlusXPowerY {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] [DecidableEq F]
    (Q : CBivariate F) (f : CPolynomial F) (t : Nat) : CBivariate F
```

`CompPoly.GuruswamiSudan.substituteYPolynomialPlusXPowerYTruncated` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean#L53))

> Truncated substitution `Y = f(X) + X^t Y`, keeping only `X`-degree `< N`
> after each accumulated `Y`-coefficient contribution.

```lean
def substituteYPolynomialPlusXPowerYTruncated {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] [DecidableEq F]
    (Q : CBivariate F) (f : CPolynomial F) (t N : Nat) : CBivariate F
```

## Depends on

- [Guruswami-Sudan Polynomial Helpers](../polynomial.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/ShiftedSubstitution.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.ShiftedSubstitution.json)
