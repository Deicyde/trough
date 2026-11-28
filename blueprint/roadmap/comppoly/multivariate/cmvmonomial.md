---
catalog: module
lean: CPoly.CMvMonomial, CPoly.CMvMonomial.ext, CPoly.CMvMonomial.extend, CPoly.CMvMonomial.totalDegree, CPoly.CMvMonomial.degreeOf, CPoly.CMvMonomial.zero, CPoly.CMvMonomial.add, CPoly.CMvMonomial.getElem_add, CPoly.CMvMonomial.add_zero, CPoly.CMvMonomial.divides, CPoly.CMvMonomial.dvd_iff_divides, CPoly.CMvMonomial.dvd_iff, CPoly.CMvMonomial.div, CPoly.CMvMonomial.getElem_div, CPoly.CMvMonomial.add_div_of_dvd, CPoly.CMvMonomial.dvd_iff_exists_add, CPoly.CMvMonomial.toFinsupp, CPoly.CMvMonomial.ofFinsupp, CPoly.CMvMonomial.ofFinsupp_toFinsupp, CPoly.CMvMonomial.toFinsupp_ofFinsupp, CPoly.CMvMonomial.dvd_iff_toFinsupp_le, CPoly.CMvMonomial.injective_ofFinsupp, CPoly.CMvMonomial.injective_toFinsupp, CPoly.CMvMonomial.equivFinsupp, CPoly.CMvMonomial.map_mul, CPoly.MonoR, CPoly.MonoR.C, CPoly.MonoR.divides, CPoly.MonoR.evalMonomial, Finsupp.ofCMvMonomial, Finsupp.toCMvMonomial
statement: formalized
proof: formalized
---

# Computable monomials

`CompPoly.Multivariate.CMvMonomial`, in [CompPoly/Multivariate/CMvMonomial.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa.

> Monomials of the form `X₀ᵃ * X₁ᵇ * ... * Xₖᶻ`. These are represented as vectors of natural numbers,
> where each element corresponds to the exponent of a variable.
>
> ## Main definitions
>
> * `CPoly.CMvMonomial n`: The type of monomials in `n` variables, implemented as `Vector ℕ n`.

`CPoly.CMvMonomial` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L36))

> Monomial in `n` variables.
> - `#v[e₀, e₁, e₂]` denotes X₀^e₀ * X₁^e₁ * X₂^e₂

```lean
def CMvMonomial (n : ℕ) : Type
```

`CPoly.CMvMonomial.ext` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L80))

```lean
protected theorem ext (h : (i : Nat) → (_ : i < n) → m₁[i] = m₂[i]) : m₁ = m₂
```

`CPoly.CMvMonomial.extend` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L84))

> Extend a monomial to a larger number of variables by padding with zeros.

```lean
def extend (n' : ℕ) (m : CMvMonomial n) : CMvMonomial (max n n')
```

`CPoly.CMvMonomial.totalDegree` (definition, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L94))

> The total degree of a monomial (sum of all exponents).

```lean
def totalDegree (m : CMvMonomial n) : ℕ
```

`CPoly.CMvMonomial.degreeOf` (definition, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L97))

> The degree of the $i$-th variable in the monomial.

```lean
def degreeOf (m : CMvMonomial n) (i : Fin n) : ℕ
```

`CPoly.CMvMonomial.zero` (definition, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L100))

> The zero monomial (all exponents are zero).

```lean
def zero : CMvMonomial n
```

`CPoly.CMvMonomial.add` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L105))

> Monomial multiplication (adds exponents element-wise).

```lean
def add : CMvMonomial n → CMvMonomial n → CMvMonomial n
```

`CPoly.CMvMonomial.getElem_add` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L111))

```lean
theorem getElem_add (i : ℕ) (h : i < n) : (m₁ + m₂)[i] = m₁[i] + m₂[i]
```

`CPoly.CMvMonomial.add_zero` (lemma, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L115))

```lean
lemma add_zero : m + 0 = m
```

`CPoly.CMvMonomial.divides` (definition, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L118))

> Check if $m_1$ divides $m_2$ (true if all exponents of $m_1$ are $\le$ those of $m_2$).

```lean
def divides (m₁ m₂ : CMvMonomial n) : Bool
```

`CPoly.CMvMonomial.dvd_iff_divides` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L125))

```lean
theorem dvd_iff_divides : m₁ ∣ m₂ ↔ divides m₁ m₂ = true
```

`CPoly.CMvMonomial.dvd_iff` (theorem, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L129))

> `m₁ ∣ m₂` holds exactly when every exponent of `m₁` is at most the matching exponent of
> `m₂`.

```lean
theorem dvd_iff : m₁ ∣ m₂ ↔ ∀ (i : ℕ) (h : i < n), m₁[i] ≤ m₂[i]
```

`CPoly.CMvMonomial.div` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L137))

> The monomial division $m_1 / m_2$ (subtracts exponents element-wise).
>
> The result makes sense assuming  `m₂ | m₁`.

```lean
def div (m₁ m₂ : CMvMonomial n) : CMvMonomial n
```

`CPoly.CMvMonomial.getElem_div` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L143))

```lean
theorem getElem_div (i : ℕ) (h : i < n) : (m₁ / m₂)[i] = m₁[i] - m₂[i]
```

`CPoly.CMvMonomial.add_div_of_dvd` (theorem, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L146))

```lean
theorem add_div_of_dvd (h : m₁ ∣ m₂) : m₁ + m₂ / m₁ = m₂
```

`CPoly.CMvMonomial.dvd_iff_exists_add` (theorem, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L152))

> Divisibility agrees with monomial multiplication, which adds exponents.

```lean
theorem dvd_iff_exists_add : m₁ ∣ m₂ ↔ ∃ c, m₂ = m₁ + c
```

`CPoly.CMvMonomial.toFinsupp` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L160))

> Convert a `CMvMonomial` to a `Finsupp`.

```lean
def toFinsupp (m : CMvMonomial n) : Fin n →₀ ℕ
```

`CPoly.CMvMonomial.ofFinsupp` (definition, [line 164](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L164))

> Convert a `Finsupp` to a `CMvMonomial`.

```lean
def ofFinsupp (m : Fin n →₀ ℕ) : CPoly.CMvMonomial n
```

`CPoly.CMvMonomial.ofFinsupp_toFinsupp` (theorem, [line 167](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L167))

```lean
theorem ofFinsupp_toFinsupp : ofFinsupp m.toFinsupp = m
```

`CPoly.CMvMonomial.toFinsupp_ofFinsupp` (theorem, [line 174](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L174))

```lean
theorem toFinsupp_ofFinsupp {m : Fin n →₀ ℕ} : (ofFinsupp m).toFinsupp = m
```

`CPoly.CMvMonomial.dvd_iff_toFinsupp_le` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L178))

> Divisibility is the pointwise order on exponent vectors.

```lean
theorem dvd_iff_toFinsupp_le : m₁ ∣ m₂ ↔ m₁.toFinsupp ≤ m₂.toFinsupp
```

`CPoly.CMvMonomial.injective_ofFinsupp` (lemma, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L182))

```lean
lemma injective_ofFinsupp : Function.Injective (ofFinsupp (n := n))
```

`CPoly.CMvMonomial.injective_toFinsupp` (lemma, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L185))

```lean
lemma injective_toFinsupp : Function.Injective (toFinsupp (n := n))
```

`CPoly.CMvMonomial.equivFinsupp` (definition, [line 188](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L188))

```lean
def equivFinsupp : CMvMonomial n ≃ (Fin n →₀ ℕ)
```

`CPoly.CMvMonomial.map_mul` (lemma, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L195))

```lean
lemma map_mul {m₁ m₂ : Multiplicative (Fin n →₀ ℕ)} :
    ofFinsupp (m₁ * m₂) = (ofFinsupp m₁) + (ofFinsupp m₂)
```

`CPoly.MonoR` (abbreviation, [line 205](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L205))

```lean
abbrev MonoR (n : ℕ) (R : Type*)
```

`CPoly.MonoR.C` (definition, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L221))

```lean
def C (c : R) : MonoR n R
```

`CPoly.MonoR.divides` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L227))

> Check if $t_1$ divides $t_2$: the monomial of $t_1$ divides that of $t_2$, and the
> coefficient of $t_2$ is zero modulo that of $t_1$.

```lean
def divides (t₁ t₂ : MonoR n R) : Bool
```

`CPoly.MonoR.evalMonomial` (definition, [line 238](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L238))

```lean
def evalMonomial {R : Type*} {n : ℕ} [CommSemiring R] : (Fin n → R) → CMvMonomial n → R
```

`Finsupp.ofCMvMonomial` (alias, [line 246](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L246))

```lean
alias Finsupp.ofCMvMonomial
```

`Finsupp.toCMvMonomial` (alias, [line 249](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean#L249))

```lean
alias Finsupp.toCMvMonomial
```

## Depends on

Its statements use no other CompPoly module's declarations.

## Sources

- [CompPoly/Multivariate/CMvMonomial.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/CMvMonomial.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.CMvMonomial.json)
