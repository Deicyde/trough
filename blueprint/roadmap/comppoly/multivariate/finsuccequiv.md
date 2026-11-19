---
catalog: module
lean: CPoly.polynomialCMvPolyEquiv, CMvPolynomial.finSuccEquiv, CMvPolynomial.finSuccEquiv_symm_apply_apply, CMvPolynomial.finSuccEquiv_apply_symm_apply, CMvPolynomial.finSuccEquiv_add, CMvPolynomial.finSuccEquiv_mul, CMvPolynomial.finSuccEquiv_zero, CMvPolynomial.finSuccEquiv_one, CPoly.CMvPolynomial.fseVars, CPoly.CMvPolynomial.fseVars_same, CPoly.CMvPolynomial.fseVars_succAbove, CPoly.CMvPolynomial.finSuccEquivNthHom, CPoly.CMvPolynomial.insertVarHom, CPoly.CMvPolynomial.finSuccEquivNthInvHom, CPoly.CMvPolynomial.finSuccEquivNthHom_C, CPoly.CMvPolynomial.finSuccEquivNthHom_X_same, CPoly.CMvPolynomial.finSuccEquivNthHom_X_succAbove, CPoly.CMvPolynomial.insertVarHom_C, CPoly.CMvPolynomial.insertVarHom_X, CPoly.CMvPolynomial.finSuccEquivNthInvHom_C, CPoly.CMvPolynomial.finSuccEquivNthInvHom_X, CPoly.CMvPolynomial.finSuccEquivNthHom_comp_insertVarHom, CPoly.CMvPolynomial.finSuccEquivNthHom_comp_inv, CPoly.CMvPolynomial.finSuccEquivNthInvHom_comp_fwd, CPoly.CMvPolynomial.finSuccEquivNth, CPoly.CMvPolynomial.finSuccEquivNth_apply, CPoly.CMvPolynomial.finSuccEquivNth_symm_apply, CPoly.CMvPolynomial.map_polyRingEquiv_toPoly_finSuccEquivNth, CPoly.CMvPolynomial.natDegree_finSuccEquivNthHom, CPoly.CMvPolynomial.natDegree_finSuccEquivNthHom_le
statement: formalized
proof: formalized
---

# `finSuccEquiv` for `CMvPolynomial`

`CompPoly.Multivariate.FinSuccEquiv`, in [CompPoly/Multivariate/FinSuccEquiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean), by Elias Judin, Aristotle (Harmonic), Dimitris Mitsios, Julian Sutherland.

> This file defines the computable multivariate polynomial equivalence for
> splitting off one variable, mirroring `MvPolynomial.finSuccEquiv` from Mathlib.
>
> In Mathlib, `MvPolynomial` accepts a general type `σ` for the index set of the
> variables. Then, `optionEquivLeft` provides the algebra isomorphism
> `MvPolynomial (Option σ) R ≃ₐ[R] Polynomial (MvPolynomial σ R)`. Finally,
> `finSuccEquiv` is defined as the composition of the rename step
> (`Fin (n+1) ≃ Option (Fin n)`) with `optionEquivLeft`. There is no such
> distinction in `CMvPolynomial` because the variables are of type `Fin n` by
> definition. Therefore, only `CMvPolynomial.finSuccEquiv` applies.
>
> ## Main definitions
>
> * `CMvPolynomial.finSuccEquiv` — `noncomputable` ring equivalence
>     `CMvPolynomial (n+1) R ≃+* Polynomial (CMvPolynomial n R)`,
>     viewing a polynomial in `n+1` variables as a univariate polynomial over `n` variables.
> * `CMvPolynomial.finSuccEquivNth p` — **computable** ring equivalence
>     `CMvPolynomial (n+1) R ≃+* CompPoly.CPolynomial (CMvPolynomial n R)` for an *arbitrary* pivot
>     `p`, splitting off variable `p`. Both directions are `eval₂` folds, so they compute; the
>     ring-equivalence laws are proved by extensionality on the `C`/`X` generators.
> * `CMvPolynomial.finSuccEquivNthHom p` / `finSuccEquivNthInvHom p` — its two directions as
>     `RingHom`s.
>
> ## Implementation notes
>
> `finSuccEquiv` is `noncomputable` because it goes through the `polyRingEquiv` bridge between
> `CMvPolynomial` and `MvPolynomial`; its forward/inverse correctness is obtained structurally from
> the underlying Mathlib `AlgEquiv` via `RingEquiv.trans`.
>
> `finSuccEquivNth` avoids that bridge in its *definition* (staying inside the computable
> `CMvPolynomial` / `CPolynomial` world), and only crosses to Mathlib in the *proof* of
> `map_polyRingEquiv_toPoly_finSuccEquivNth`, which identifies it with
> `MvPolynomial.finSuccEquivNth` after transport.

> ### Polynomial-level ring equivalence

`CPoly.polynomialCMvPolyEquiv` (definition, [line 64](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L64))

> `Polynomial.mapEquiv` through the CMvPolynomial ↔ MvPolynomial bridge.

```lean
noncomputable def polynomialCMvPolyEquiv :
    Polynomial (CMvPolynomial n R) ≃+* Polynomial (MvPolynomial (Fin n) R)
```

> ### `finSuccEquiv`

`CMvPolynomial.finSuccEquiv` (definition, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L80))

> Ring equivalence splitting off the first variable:
> `CMvPolynomial (n+1) R ≃+* Polynomial (CMvPolynomial n R)`.
>
> This mirrors `MvPolynomial.finSuccEquiv R n`. The 0-th variable becomes
> the univariate indeterminate `Polynomial.X`, and variables `1, …, n` become
> the multivariate variables of the coefficient ring `CMvPolynomial n R`.

```lean
noncomputable def finSuccEquiv :
    CMvPolynomial (n + 1) R ≃+* Polynomial (CMvPolynomial n R)
```

`CMvPolynomial.finSuccEquiv_symm_apply_apply` (theorem, [line 87](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L87))

> The equivalence is a left inverse: applying the inverse then forward is the identity.

```lean
theorem finSuccEquiv_symm_apply_apply (p : CMvPolynomial (n + 1) R) :
    finSuccEquiv.symm (finSuccEquiv p) = p
```

`CMvPolynomial.finSuccEquiv_apply_symm_apply` (theorem, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L93))

> The equivalence is a right inverse: applying forward then the inverse is the identity.

```lean
theorem finSuccEquiv_apply_symm_apply
    (q : Polynomial (CMvPolynomial n R)) :
    finSuccEquiv (finSuccEquiv.symm q) = q
```

`CMvPolynomial.finSuccEquiv_add` (theorem, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L99))

> `finSuccEquiv` preserves addition.

```lean
theorem finSuccEquiv_add (p q : CMvPolynomial (n + 1) R) :
    finSuccEquiv (p + q) =
      finSuccEquiv p + finSuccEquiv q
```

`CMvPolynomial.finSuccEquiv_mul` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L105))

> `finSuccEquiv` preserves multiplication.

```lean
theorem finSuccEquiv_mul (p q : CMvPolynomial (n + 1) R) :
    finSuccEquiv (p * q) =
      finSuccEquiv p * finSuccEquiv q
```

`CMvPolynomial.finSuccEquiv_zero` (theorem, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L112))

> `finSuccEquiv` maps zero to zero.

```lean
theorem finSuccEquiv_zero :
    finSuccEquiv (0 : CMvPolynomial (n + 1) R) = 0
```

`CMvPolynomial.finSuccEquiv_one` (theorem, [line 118](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L118))

> `finSuccEquiv` maps one to one.

```lean
theorem finSuccEquiv_one :
    finSuccEquiv (1 : CMvPolynomial (n + 1) R) = 1
```

> ### The computable `finSuccEquivNth` (arbitrary pivot)
>
> Unlike `finSuccEquiv` above, this stays inside the computable `CMvPolynomial` / `CPolynomial`
> world and works for an arbitrary pivot `p`.

`CPoly.CMvPolynomial.fseVars` (definition, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L137))

> Assignment used by the forward direction: variable `p` goes to the univariate `X`, every
> other variable `p.succAbove j` goes to the constant `C (X j)`.

```lean
def fseVars (p : Fin (n + 1)) : Fin (n + 1) → CPolynomial (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.fseVars_same` (theorem, [line 140](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L140))

```lean
theorem fseVars_same (p : Fin (n + 1)) :
    fseVars (R := R) p p = CPolynomial.X
```

`CPoly.CMvPolynomial.fseVars_succAbove` (theorem, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L143))

```lean
theorem fseVars_succAbove (p : Fin (n + 1)) (j : Fin n) :
    fseVars (R := R) p (p.succAbove j) = CPolynomial.C (CMvPolynomial.X j)
```

`CPoly.CMvPolynomial.finSuccEquivNthHom` (definition, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L148))

> Forward direction of `finSuccEquivNth`, as a `RingHom`.  Splits variable `p` off as the
> univariate indeterminate over the other `n` variables.  Computable.

```lean
def finSuccEquivNthHom (p : Fin (n + 1)) :
    CMvPolynomial (n + 1) R →+* CPolynomial (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.insertVarHom` (definition, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L154))

> "Insert a dummy variable at position `p`": the embedding `CMvPolynomial n R →+* CMvPolynomial
> (n+1) R` sending `X j` to `X (p.succAbove j)`.  Computable.

```lean
def insertVarHom (p : Fin (n + 1)) : CMvPolynomial n R →+* CMvPolynomial (n + 1) R
```

`CPoly.CMvPolynomial.finSuccEquivNthInvHom` (definition, [line 158](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L158))

> Inverse direction of `finSuccEquivNth`, as a `RingHom`.  Computable.

```lean
def finSuccEquivNthInvHom (p : Fin (n + 1)) :
    CPolynomial (CMvPolynomial n R) →+* CMvPolynomial (n + 1) R
```

`CPoly.CMvPolynomial.finSuccEquivNthHom_C` (theorem, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L162))

```lean
theorem finSuccEquivNthHom_C (p : Fin (n + 1)) (c : R) :
    finSuccEquivNthHom (R := R) p (CMvPolynomial.C c) = CPolynomial.C (CMvPolynomial.C c)
```

`CPoly.CMvPolynomial.finSuccEquivNthHom_X_same` (theorem, [line 166](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L166))

```lean
theorem finSuccEquivNthHom_X_same (p : Fin (n + 1)) :
    finSuccEquivNthHom (R := R) p (CMvPolynomial.X p) = CPolynomial.X
```

`CPoly.CMvPolynomial.finSuccEquivNthHom_X_succAbove` (theorem, [line 170](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L170))

```lean
theorem finSuccEquivNthHom_X_succAbove (p : Fin (n + 1)) (j : Fin n) :
    finSuccEquivNthHom (R := R) p (CMvPolynomial.X (p.succAbove j))
      = CPolynomial.C (CMvPolynomial.X j)
```

`CPoly.CMvPolynomial.insertVarHom_C` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L176))

```lean
theorem insertVarHom_C (p : Fin (n + 1)) (c : R) :
    insertVarHom (R := R) p (CMvPolynomial.C c) = CMvPolynomial.C c
```

`CPoly.CMvPolynomial.insertVarHom_X` (theorem, [line 181](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L181))

```lean
theorem insertVarHom_X (p : Fin (n + 1)) (j : Fin n) :
    insertVarHom (R := R) p (CMvPolynomial.X j) = CMvPolynomial.X (p.succAbove j)
```

`CPoly.CMvPolynomial.finSuccEquivNthInvHom_C` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L185))

```lean
theorem finSuccEquivNthInvHom_C (p : Fin (n + 1)) (q : CMvPolynomial n R) :
    finSuccEquivNthInvHom (R := R) p (CPolynomial.C q) = insertVarHom p q
```

`CPoly.CMvPolynomial.finSuccEquivNthInvHom_X` (theorem, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L189))

```lean
theorem finSuccEquivNthInvHom_X (p : Fin (n + 1)) :
    finSuccEquivNthInvHom (R := R) p (CPolynomial.X) = CMvPolynomial.X p
```

`CPoly.CMvPolynomial.finSuccEquivNthHom_comp_insertVarHom` (theorem, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L195))

> `finSuccEquivNthHom` composed with `insertVarHom` is the constant embedding
> `CMvPolynomial n R →+* CPolynomial (CMvPolynomial n R)`.

```lean
theorem finSuccEquivNthHom_comp_insertVarHom (p : Fin (n + 1)) :
    (finSuccEquivNthHom (R := R) p).comp (insertVarHom p) = CPolynomial.CHom
```

`CPoly.CMvPolynomial.finSuccEquivNthHom_comp_inv` (theorem, [line 202](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L202))

```lean
theorem finSuccEquivNthHom_comp_inv (p : Fin (n + 1)) :
    (finSuccEquivNthHom (R := R) p).comp (finSuccEquivNthInvHom p)
      = RingHom.id (CPolynomial (CMvPolynomial n R))
```

`CPoly.CMvPolynomial.finSuccEquivNthInvHom_comp_fwd` (theorem, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L210))

```lean
theorem finSuccEquivNthInvHom_comp_fwd (p : Fin (n + 1)) :
    (finSuccEquivNthInvHom (R := R) p).comp (finSuccEquivNthHom p)
      = RingHom.id (CMvPolynomial (n + 1) R)
```

`CPoly.CMvPolynomial.finSuccEquivNth` (definition, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L225))

> **The computable `finSuccEquivNth`**: a ring equivalence
> `CMvPolynomial (n+1) R ≃+* CompPoly.CPolynomial (CMvPolynomial n R)` for an arbitrary pivot `p`.
> Both directions compute.

```lean
def finSuccEquivNth (p : Fin (n + 1)) :
    CMvPolynomial (n + 1) R ≃+* CPolynomial (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.finSuccEquivNth_apply` (theorem, [line 230](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L230))

```lean
theorem finSuccEquivNth_apply (p : Fin (n + 1)) (P : CMvPolynomial (n + 1) R) :
    finSuccEquivNth p P = finSuccEquivNthHom p P
```

`CPoly.CMvPolynomial.finSuccEquivNth_symm_apply` (theorem, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L233))

```lean
theorem finSuccEquivNth_symm_apply (p : Fin (n + 1))
    (Q : CPolynomial (CMvPolynomial n R)) :
    (finSuccEquivNth p).symm Q = finSuccEquivNthInvHom p Q
```

> ### Compatibility with Mathlib's `MvPolynomial.finSuccEquivNth`

`CPoly.CMvPolynomial.map_polyRingEquiv_toPoly_finSuccEquivNth` (theorem, [line 241](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L241))

> The computable `finSuccEquivNth`, transported to Mathlib's `MvPolynomial`/`Polynomial` world
> along `polyRingEquiv` and `CPolynomial.toPoly`, is Mathlib's `MvPolynomial.finSuccEquivNth`.

```lean
theorem map_polyRingEquiv_toPoly_finSuccEquivNth (p : Fin (n + 1)) (P : CMvPolynomial (n + 1) R) :
    Polynomial.map (CPoly.polyRingEquiv (n := n) (R := R)).toRingHom
        (CPolynomial.toPoly (finSuccEquivNthHom p P))
      = MvPolynomial.finSuccEquivNth R p (CPoly.fromCMvPolynomial P)
```

`CPoly.CMvPolynomial.natDegree_finSuccEquivNthHom` (theorem, [line 279](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L279))

> The univariate degree of `finSuccEquivNth p P` is the degree of variable `p` in `P`.

```lean
theorem natDegree_finSuccEquivNthHom (p : Fin (n + 1)) (P : CMvPolynomial (n + 1) R) :
    (finSuccEquivNthHom p P).natDegree = P.degreeOf p
```

`CPoly.CMvPolynomial.natDegree_finSuccEquivNthHom_le` (theorem, [line 291](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean#L291))

> `finSuccEquivNth p P` has univariate degree at most `d` whenever `P` has per-variable
> degree at most `d`.

```lean
theorem natDegree_finSuccEquivNthHom_le {d : ℕ} (p : Fin (n + 1)) (P : CMvPolynomial (n + 1) R)
    (hP : ∀ k, P.degreeOf k ≤ d) : (finSuccEquivNthHom p P).natDegree ≤ d
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Evaluation](mvpolyequiv/eval.md)
- [MvPolynomial Equiv](../tomathlib/mvpolynomial/equiv.md)
- [`C`, `eval₂`, and coefficient-mapping as ring homomorphisms](../univariate/part-02/topoly/ringhom.md)

## Proof depends on

- [Computable multivariate polynomials (extended operations)](operations.md)

## Sources

- [CompPoly/Multivariate/FinSuccEquiv.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Multivariate/FinSuccEquiv.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.FinSuccEquiv.json)
