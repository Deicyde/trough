---
catalog: module
lean: CPoly.list_foldl_add_comm, CPoly.foldl_add_comm', CPoly.toFinsupp_apply, CPoly.renameMonomial_eq, CPoly.fromCMvPolynomial_monomial, CPoly.fromCMvPolynomial_finsupp_sum, CPoly.fromCMvPolynomial_rename, CPoly.C_eq_monomial, CPoly.toFinsupp_zero, CPoly.fromCMvPolynomial_C, CPoly.rename_C, CPoly.X_eq_monomial, CPoly.toFinsupp_unitMono, CPoly.fromCMvPolynomial_X, CPoly.rename_X, CPoly.rename_add, CPoly.rename_mul, CPoly.rename_id, CPoly.rename_rename, CMvPolynomial.renameEquiv
statement: formalized
proof: formalized
---

# Properties of variable renaming for `CMvPolynomial`

`CompPoly.Multivariate.Rename`, in [CompPoly/Multivariate/Rename.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean), by Dimitris Mitsios.

> This file proves properties of the `rename` function defined in `CMvPolynomial.lean`,
> by transferring results from Mathlib's `MvPolynomial.rename` through the
> `polyRingEquiv : CMvPolynomial n R ≃+* MvPolynomial (Fin n) R` equivalence.
>
> ## Main results
>
> * `fromCMvPolynomial_rename` — correspondence between `CMvPolynomial.rename` and
>   `MvPolynomial.rename`
> * `rename_C`, `rename_X`, `rename_add`, `rename_mul`, `rename_id`, `rename_rename`
>   — algebraic properties
> * `CMvPolynomial.renameEquiv` — ring isomorphism for bijective variable renaming

> ### Helper lemmas for `fromCMvPolynomial_rename`

`CPoly.list_foldl_add_comm` (lemma, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L40))

> In a commutative additive monoid, the order of addition in a list fold
> does not matter.

```lean
lemma list_foldl_add_comm {β K V : Type*} [AddCommMonoid β]
    (g : K → V → β) (l : List (K × V)) (init : β) :
    List.foldl (fun acc pair => acc + g pair.1 pair.2) init l =
    List.foldl (fun acc pair => g pair.1 pair.2 + acc) init l
```

`CPoly.foldl_add_comm'` (lemma, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L52))

> Swapping addition order in `ExtTreeMap.foldl` does not change the result.

```lean
lemma foldl_add_comm' {β : Type*} [AddCommMonoid β] {k : ℕ}
    {R' : Type*} (g : CMvMonomial k → R' → β)
    (t : Std.ExtTreeMap (CMvMonomial k) R') :
    Std.ExtTreeMap.foldl (fun acc m c => acc + g m c) (0 : β) t =
    Std.ExtTreeMap.foldl (fun acc m c => g m c + acc) (0 : β) t
```

`CPoly.toFinsupp_apply` (lemma, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L61))

> Applying `CMvMonomial.toFinsupp` at index `i` equals `Vector.get`.

```lean
lemma toFinsupp_apply (mono : CMvMonomial n) (i : Fin n) :
    (CMvMonomial.toFinsupp mono) i = mono.get i
```

`CPoly.renameMonomial_eq` (lemma, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L66))

> Monomial renaming via `Vector.ofFn` corresponds to `Finsupp.mapDomain`
> on the `Finsupp` side.

```lean
lemma renameMonomial_eq (f : Fin n → Fin m) (mono : CMvMonomial n) :
    (Vector.ofFn (fun j => (Finset.univ.filter (fun i => f i = j)).sum
      (fun i => mono.get i)) : CMvMonomial m) =
    CMvMonomial.ofFinsupp
      (Finsupp.mapDomain f (CMvMonomial.toFinsupp mono))
```

`CPoly.fromCMvPolynomial_monomial` (lemma, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L85))

> `fromCMvPolynomial` maps `CMvPolynomial.monomial` to
> `MvPolynomial.monomial`.

```lean
lemma fromCMvPolynomial_monomial {k : ℕ} (mono : CMvMonomial k) (c : R) :
    fromCMvPolynomial (CMvPolynomial.monomial mono c) =
    MvPolynomial.monomial (CMvMonomial.toFinsupp mono) c
```

`CPoly.fromCMvPolynomial_finsupp_sum` (lemma, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L112))

> `fromCMvPolynomial` distributes over `Finsupp.sum`.

```lean
lemma fromCMvPolynomial_finsupp_sum {k : ℕ}
    (g : (Fin n →₀ ℕ) → R → CMvPolynomial k R)
    (a : CMvPolynomial n R) :
    fromCMvPolynomial (Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial a)) g) =
    Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial a))
      (fun μ c => fromCMvPolynomial (g μ c))
```

> ### Main correspondence lemma

`CPoly.fromCMvPolynomial_rename` (lemma, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L125))

> `CMvPolynomial.rename` agrees with `MvPolynomial.rename` under the
> `fromCMvPolynomial` equivalence.

```lean
lemma fromCMvPolynomial_rename (f : Fin n → Fin m)
    (p : CMvPolynomial n R) :
    fromCMvPolynomial (CMvPolynomial.rename f p) =
    MvPolynomial.rename f (fromCMvPolynomial p)
```

> ### Bridging lemmas for `C` and `X`

`CPoly.C_eq_monomial` (lemma, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L162))

> `CMvPolynomial.C c` equals `CMvPolynomial.monomial 0 c`.

```lean
lemma C_eq_monomial {k : ℕ} (c : R) :
    CMvPolynomial.C (n := k) c = CMvPolynomial.monomial 0 c
```

`CPoly.toFinsupp_zero` (lemma, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L183))

> The `Finsupp` of the zero monomial is zero.

```lean
lemma toFinsupp_zero {k : ℕ} :
    CMvMonomial.toFinsupp (0 : CMvMonomial k) = 0
```

`CPoly.fromCMvPolynomial_C` (lemma, [line 190](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L190))

> `fromCMvPolynomial` maps `CMvPolynomial.C` to `MvPolynomial.C`.

```lean
lemma fromCMvPolynomial_C {k : ℕ} (c : R) :
    fromCMvPolynomial (CMvPolynomial.C (n := k) c) =
    MvPolynomial.C c
```

> ### Algebraic properties of rename

`CPoly.rename_C` (lemma, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L200))

> Constants are unchanged under renaming.

```lean
lemma rename_C (f : Fin n → Fin m) (c : R) :
    CMvPolynomial.rename f (CMvPolynomial.C c) =
    CMvPolynomial.C (n := m) c
```

`CPoly.X_eq_monomial` (lemma, [line 210](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L210))

> `CMvPolynomial.X i` equals `CMvPolynomial.monomial eᵢ 1`
> where `eᵢ` is the `i`-th standard basis vector.

```lean
lemma X_eq_monomial {k : ℕ} (i : Fin k) :
    CMvPolynomial.X (R := R) i = CMvPolynomial.monomial
      (Vector.ofFn (fun j => if j = i then 1 else 0))
      (1 : R)
```

`CPoly.toFinsupp_unitMono` (lemma, [line 223](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L223))

> The `Finsupp` of the `i`-th standard basis monomial is
> `Finsupp.single i 1`.

```lean
lemma toFinsupp_unitMono {k : ℕ} (i : Fin k) :
    CMvMonomial.toFinsupp
      (Vector.ofFn (fun j : Fin k =>
        if j = i then 1 else 0)) =
    Finsupp.single i 1
```

`CPoly.fromCMvPolynomial_X` (lemma, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L235))

> `fromCMvPolynomial` maps `CMvPolynomial.X i` to
> `MvPolynomial.X i`.

```lean
lemma fromCMvPolynomial_X {k : ℕ} (i : Fin k) :
    fromCMvPolynomial (CMvPolynomial.X (R := R) i) =
    MvPolynomial.X i
```

`CPoly.rename_X` (lemma, [line 244](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L244))

> Renaming maps variable `X i` to `X (f i)`.

```lean
lemma rename_X (f : Fin n → Fin m) (i : Fin n) :
    CMvPolynomial.rename f (CMvPolynomial.X (R := R) i) =
    CMvPolynomial.X (f i)
```

`CPoly.rename_add` (lemma, [line 254](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L254))

> Renaming preserves addition.

```lean
lemma rename_add (f : Fin n → Fin m)
    (p q : CMvPolynomial n R) :
    CMvPolynomial.rename f (p + q) =
    CMvPolynomial.rename f p +
    CMvPolynomial.rename f q
```

`CPoly.rename_mul` (lemma, [line 266](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L266))

> Renaming preserves multiplication.

```lean
lemma rename_mul (f : Fin n → Fin m)
    (p q : CMvPolynomial n R) :
    CMvPolynomial.rename f (p * q) =
    CMvPolynomial.rename f p *
    CMvPolynomial.rename f q
```

`CPoly.rename_id` (lemma, [line 278](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L278))

> Renaming by the identity function is the identity.

```lean
lemma rename_id (p : CMvPolynomial n R) :
    CMvPolynomial.rename id p = p
```

`CPoly.rename_rename` (lemma, [line 286](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L286))

> Composing two renamings equals renaming by the composition.

```lean
lemma rename_rename {k : ℕ} (f : Fin n → Fin m)
    (g : Fin m → Fin k) (p : CMvPolynomial n R) :
    CMvPolynomial.rename g (CMvPolynomial.rename f p) =
    CMvPolynomial.rename (g ∘ f) p
```

`CMvPolynomial.renameEquiv` (definition, [line 305](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean#L305))

> Ring equivalence for variable renaming when the function is
> a bijection.

```lean
noncomputable def renameEquiv
    (f : Fin n ≃ Fin m) :
    CMvPolynomial n R ≃+* CMvPolynomial m R
```

## Depends on

- [Computable multivariate polynomials (extended operations)](operations.md)

## Sources

- [CompPoly/Multivariate/Rename.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/Rename.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multivariate.Rename.json)
