---
catalog: module
lean: CompPoly.GuruswamiSudan.RootMod, CompPoly.GuruswamiSudan.MatchesPrefix, CompPoly.GuruswamiSudan.MatchesRootPrefix, CompPoly.GuruswamiSudan.SubstitutionDegreeBound
statement: formalized
proof: formalized
---

# Alekhnovich Root Search Lemmas

`CompPoly.Bivariate.GuruswamiSudan.Root.Alekhnovich.Lemmas`, in [CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean), by Valerii Huhnin.

> Proof support for the Alekhnovich bounded bivariate root backend.

`CompPoly.GuruswamiSudan.RootMod` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean#L26))

> `p` is a root of `Q` modulo `X^N`, stated as finitely many coefficient
> equalities.

```lean
def RootMod {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (Q : CBivariate F) (p : CPolynomial F) (N : Nat) : Prop
```

`CompPoly.GuruswamiSudan.MatchesPrefix` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean#L32))

> `f` matches the first `t` coefficients of `p`.

```lean
def MatchesPrefix {F : Type*} [Zero F] [BEq F] [LawfulBEq F]
    (p f : CPolynomial F) (t : Nat) : Prop
```

`CompPoly.GuruswamiSudan.MatchesRootPrefix` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean#L38))

> `rp` is a root-prefix record matching the first `rp.precision` coefficients
> of `p`.

```lean
def MatchesRootPrefix {F : Type*} [Zero F] [BEq F] [LawfulBEq F]
    (p : CPolynomial F) (rp : RootPrefix F) : Prop
```

`CompPoly.GuruswamiSudan.SubstitutionDegreeBound` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean#L44))

> Logical exactness bound for substituting any `degree < k` univariate
> polynomial into `Q`.

```lean
def SubstitutionDegreeBound {F : Type*} [Zero F] [BEq F]
    (Q : CBivariate F) (k N : Nat) : Prop
```

## Depends on

- [Alekhnovich Bivariate Bounded Root Search](algorithm.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Root/Alekhnovich/Lemmas.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Root.Alekhnovich.Lemmas.json)
