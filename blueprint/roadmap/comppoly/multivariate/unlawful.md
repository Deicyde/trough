---
catalog: module
lean: CPoly.Unlawful, CPoly.Unlawful.ext_getElem?, CPoly.Unlawful.ofList, CPoly.Unlawful.extend, CPoly.Unlawful.isNoZeroCoef, CPoly.Unlawful.toFinset, CPoly.Unlawful.monomials, CPoly.Unlawful.mem_monomials, CPoly.Unlawful.C, CPoly.Unlawful.C_zero, CPoly.Unlawful.C_zero', CPoly.Unlawful.zero_eq_zero, CPoly.Unlawful.zero_eq_empty, CPoly.Unlawful.not_mem_C_zero, CPoly.Unlawful.not_mem_zero, CPoly.Unlawful.isNoZeroCoef_zero, CPoly.Unlawful.add, CPoly.Unlawful.grind_add_skip, CPoly.Unlawful.addMonoR, CPoly.Unlawful.mul₀, CPoly.Unlawful.mul₀_zero, CPoly.Unlawful.mul, CPoly.Unlawful.neg, CPoly.Unlawful.sub, CPoly.Unlawful.leadingTerm?, CPoly.Unlawful.leadingMonomial?, CPoly.Unlawful.instDecidableEq, CPoly.Unlawful.coeff, CPoly.Unlawful.filter_get, CPoly.Unlawful.add_getD?
statement: formalized
proof: formalized
---

# Unlawful multivariate polynomials

`CompPoly.Multivariate.Unlawful`, in [CompPoly/Multivariate/Unlawful.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdusa.

> This file defines the `Unlawful` type, which represents multivariate polynomials
> as a map from monomials to coefficients. Unlike `Lawful`, it does not enforce
> the absence of zero coefficients.
>
> ## Main definitions
>
> * `CPoly.Unlawful n R`: A map from `CMvMonomial n` to `R`, implemented using `Std.ExtTreeMap`.

`CPoly.Unlawful` (abbreviation, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L37))

> Polynomial in `n` variables with coefficients in `R`.
> Internally represented as a tree map from monomials to coefficients.

```lean
abbrev Unlawful (n : ℕ) (R : Type*) : Type _
```

`CPoly.Unlawful.ext_getElem?` (lemma, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L78))

```lean
lemma ext_getElem? {n R} {t₁ t₂ : Unlawful n R}
    (h : ∀ (k : CMvMonomial n), t₁[k]? = t₂[k]?) : t₁ = t₂
```

`CPoly.Unlawful.ofList` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L86))

> Construct an `Unlawful` polynomial from a list of monomial-coefficient pairs.

```lean
def ofList (l : List (CMvMonomial n × R)) : Unlawful n R
```

`CPoly.Unlawful.extend` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L89))

> Extend the number of variables by padding monomials with zeros.

```lean
def extend (n' : ℕ) (p : Unlawful n R) : Unlawful (n ⊔ n') R
```

`CPoly.Unlawful.isNoZeroCoef` (abbreviation, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L93))

> Check if the polynomial has no zero coefficients.

```lean
abbrev isNoZeroCoef [Zero R] (p : Unlawful n R) : Prop
```

`CPoly.Unlawful.toFinset` (definition, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L95))

```lean
def toFinset [DecidableEq R] (p : Unlawful n R) : Finset (CMvMonomial n × R)
```

`CPoly.Unlawful.monomials` (abbreviation, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L99))

> The list of monomials present in the polynomial.

```lean
abbrev monomials (p : Unlawful n R) : List (CMvMonomial n)
```

`CPoly.Unlawful.mem_monomials` (lemma, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L103))

```lean
lemma mem_monomials {m : CMvMonomial n} {up : Unlawful n R} :
    m ∈ up.monomials ↔ m ∈ up
```

`CPoly.Unlawful.C` (definition, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L115))

> Constant polynomial.

```lean
def C [BEq R] [LawfulBEq R] [Zero R] (c : R) : Unlawful n R
```

`CPoly.Unlawful.C_zero` (lemma, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L131))

```lean
lemma C_zero : C (n := n) (0 : R) = 0
```

`CPoly.Unlawful.C_zero'` (lemma, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L136))

```lean
lemma C_zero' : C (n := n) (0 : ℕ) = 0
```

`CPoly.Unlawful.zero_eq_zero` (lemma, [line 139](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L139))

```lean
lemma zero_eq_zero : (Zero.zero : R) = 0
```

`CPoly.Unlawful.zero_eq_empty` (lemma, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L141))

```lean
lemma zero_eq_empty [BEq R] [LawfulBEq R] : (0 : Unlawful n R) = ∅
```

`CPoly.Unlawful.not_mem_C_zero` (lemma, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L146))

```lean
lemma not_mem_C_zero : x ∉ C 0
```

`CPoly.Unlawful.not_mem_zero` (lemma, [line 153](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L153))

```lean
lemma not_mem_zero : x ∉ (0 : Unlawful n R)
```

`CPoly.Unlawful.isNoZeroCoef_zero` (lemma, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L156))

```lean
lemma isNoZeroCoef_zero : isNoZeroCoef (n := n) (R := R) 0
```

`CPoly.Unlawful.add` (definition, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L163))

> Pointwise addition of coefficients.

```lean
def add [Add R] (p₁ p₂ : Unlawful n R) : Unlawful n R
```

`CPoly.Unlawful.grind_add_skip` (lemma, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L169))

```lean
protected lemma grind_add_skip [Add R] {p₁ p₂ : Unlawful n R} :
    p₁ + p₂ = p₁.mergeWith (fun _ c₁ c₂ ↦ c₁ + c₂) p₂
```

`CPoly.Unlawful.addMonoR` (definition, [line 173](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L173))

> Add a single monomial-coefficient term to a polynomial.

```lean
def addMonoR [Add R] (p : Unlawful n R) (term : MonoR n R) : Unlawful n R
```

`CPoly.Unlawful.mul₀` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L177))

> Multiply a polynomial by a single monomial term.

```lean
def mul₀ [Mul R] (t : MonoR n R) (p : Unlawful n R) : Unlawful n R
```

`CPoly.Unlawful.mul₀_zero` (lemma, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L183))

```lean
lemma mul₀_zero [Zero R] [BEq R] [LawfulBEq R] [Mul R] {t : MonoR n R} : mul₀ t 0 = 0
```

`CPoly.Unlawful.mul` (definition, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L188))

> Polynomial multiplication using a nested fold (distributive law).

```lean
def mul [Mul R] [Add R] [Zero R] [BEq R] [LawfulBEq R] (p₁ p₂ : Unlawful n R) : Unlawful n R
```

`CPoly.Unlawful.neg` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L200))

> Negation (negates all coefficients).

```lean
def neg (p : Unlawful n R) : Unlawful n R
```

`CPoly.Unlawful.sub` (definition, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L206))

> Subtraction.

```lean
def sub [Add R] (p₁ p₂ : Unlawful n R) : Unlawful n R
```

`CPoly.Unlawful.leadingTerm?` (definition, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L214))

> Return the term with the lexicographically largest monomial.

```lean
def leadingTerm? : Unlawful n R → Option (MonoR n R)
```

`CPoly.Unlawful.leadingMonomial?` (definition, [line 218](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L218))

> Return the lexicographically largest monomial.

```lean
def leadingMonomial? : Unlawful n R → Option (CMvMonomial n)
```

`CPoly.Unlawful.instDecidableEq` (instance, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L221))

```lean
instance instDecidableEq [DecidableEq R] : DecidableEq (Unlawful n R)
```

`CPoly.Unlawful.coeff` (definition, [line 226](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L226))

```lean
def coeff {R : Type*} {n : ℕ} [Zero R] (m : CMvMonomial n) (p : Unlawful n R) : R
```

`CPoly.Unlawful.filter_get` (lemma, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L230))

```lean
lemma filter_get {R : Type*} [BEq R] [LawfulBEq R] {v : R} {m : CMvMonomial n} (a : Unlawful n R) :
    (ExtTreeMap.filter (fun _ c => c != v) a)[m]?.getD v = a[m]?.getD v
```

`CPoly.Unlawful.add_getD?` (lemma, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean#L234))

```lean
lemma add_getD? [AddZeroClass R] {m : CMvMonomial n} {p q : Unlawful n R} :
    (p.add q)[m]?.getD 0 = p[m]?.getD 0 + q[m]?.getD 0
```

## Depends on

- [Computable monomials](cmvmonomial.md)

## Proof depends on

- [Auxiliary lemmas for `Std.ExtTreeMap`](../data/exttreemap/exttreemap.md)

## Sources

- [CompPoly/Multivariate/Unlawful.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Unlawful.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Unlawful.json)
