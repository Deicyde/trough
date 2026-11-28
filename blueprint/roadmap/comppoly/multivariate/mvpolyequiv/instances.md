---
catalog: module
lean: CPoly.map_add, CPoly.map_zero, CPoly.map_one, CPoly.toList_pairs_monomial_coeff, CPoly.foldl_eq_sum, CPoly.coeff_sum, CPoly.fromCMvPolynomial_sum_eq_sum_fromCMvPolynomial, CPoly.map_mul, CPoly.map_neg, CPoly.map_sub, CPoly.polyRingEquiv, CPoly.coe_polyRingEquiv, CPoly.CMvPolynomial.isEmptyRingEquiv, CPoly.CMvPolynomial.instNontrivial, CPoly.CMvPolynomial.instSMul, CPoly.CMvPolynomial.instSMulZeroClass, CPoly.CMvPolynomial.smul_def, CPoly.CMvPolynomial.fromCMvPolynomial_C, CPoly.CMvPolynomial.CHom, CPoly.CMvPolynomial.CHom_apply, CPoly.CMvPolynomial.fromCMvPolynomial_sum, CPoly.CMvPolynomial.fromCMvPolynomial_prod, CPoly.CMvPolynomial.instAlgebra
statement: formalized
proof: formalized
---

# `CMvPolynomial`/`MvPolynomial` Instances

`CompPoly.Multivariate.MvPolyEquiv.Instances`, in [CompPoly/Multivariate/MvPolyEquiv/Instances.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean), by Frantisek Silvasi, Julian Sutherland, Andrei Burdușa, Dimitris Mitsios.

> Compatibility lemmas used to transport algebraic structure across the conversion.

`CPoly.map_add` (lemma, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L29))

```lean
lemma map_add (a b : CMvPolynomial n R) :
    fromCMvPolynomial (a + b) = fromCMvPolynomial a + fromCMvPolynomial b
```

`CPoly.map_zero` (lemma, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L79))

```lean
lemma map_zero : fromCMvPolynomial (0 : CMvPolynomial n R) = 0
```

`CPoly.map_one` (lemma, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L100))

```lean
lemma map_one : fromCMvPolynomial (1 : CMvPolynomial n R) = 1
```

`CPoly.toList_pairs_monomial_coeff` (lemma, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L182))

```lean
lemma toList_pairs_monomial_coeff {β : Type*} [AddCommMonoid β]
    {t : Unlawful n R}
  {f : CMvMonomial n → R → β} :
  t.toList.map (fun term => f term.1 term.2) =
    t.monomials.map (fun m => f m (t.coeff m))
```

`CPoly.foldl_eq_sum` (lemma, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L193))

```lean
lemma foldl_eq_sum {β : Type*} [AddCommMonoid β]
    {t : CMvPolynomial n R}
    {f : CMvMonomial n → R → β} :
    ExtTreeMap.foldl (fun x m c => (f m c) + x) 0 t.1 =
      Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial t))
        (f ∘ CMvMonomial.ofFinsupp)
```

`CPoly.coeff_sum` (lemma, [line 214](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L214))

```lean
lemma coeff_sum [AddCommMonoid α]
    (s : Finset α)
    (f : α → CMvPolynomial n R)
    (m : CMvMonomial n) :
    coeff m (∑ x ∈ s, f x) = ∑ x ∈ s, coeff m (f x)
```

`CPoly.fromCMvPolynomial_sum_eq_sum_fromCMvPolynomial` (lemma, [line 225](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L225))

```lean
lemma fromCMvPolynomial_sum_eq_sum_fromCMvPolynomial
    {f : (Fin n →₀ ℕ) → R → Lawful n R }
    {a : CMvPolynomial n R} :
    fromCMvPolynomial (Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial a)) f) =
      Finsupp.sum (AddMonoidAlgebra.coeff (fromCMvPolynomial a))
        (fun m c ↦ fromCMvPolynomial (f m c))
```

`CPoly.map_mul` (lemma, [line 235](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L235))

```lean
lemma map_mul (a b : CMvPolynomial n R) :
    fromCMvPolynomial (a * b) = fromCMvPolynomial a * fromCMvPolynomial b
```

`CPoly.map_neg` (lemma, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L339))

```lean
lemma map_neg (a : CMvPolynomial n R) :
    fromCMvPolynomial (-a) = -fromCMvPolynomial a
```

`CPoly.map_sub` (lemma, [line 352](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L352))

```lean
lemma map_sub (a b : CMvPolynomial n R) :
    fromCMvPolynomial (Sub.sub a b) = fromCMvPolynomial a - fromCMvPolynomial b
```

`CPoly.polyRingEquiv` (definition, [line 372](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L372))

```lean
noncomputable def polyRingEquiv :
  RingEquiv (CPoly.CMvPolynomial n R) (MvPolynomial (Fin n) R)
```

`CPoly.coe_polyRingEquiv` (theorem, [line 379](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L379))

> The underlying function of `polyRingEquiv` is the computable `fromCMvPolynomial`.

```lean
theorem coe_polyRingEquiv :
    ⇑(CPoly.polyRingEquiv (n := n) (R := R)) = CPoly.fromCMvPolynomial
```

`CPoly.CMvPolynomial.isEmptyRingEquiv` (definition, [line 389](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L389))

> Ring equivalence between `CMvPolynomial 0 R` and `R`.

```lean
noncomputable def isEmptyRingEquiv : CMvPolynomial 0 R ≃+* R
```

`CPoly.CMvPolynomial.instNontrivial` (instance, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L392))

```lean
instance instNontrivial [Nontrivial R] : Nontrivial (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.instSMul` (instance, [line 395](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L395))

```lean
instance instSMul : SMul R (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.instSMulZeroClass` (instance, [line 398](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L398))

```lean
instance instSMulZeroClass : SMulZeroClass R (CMvPolynomial n R)
```

`CPoly.CMvPolynomial.smul_def` (lemma, [line 402](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L402))

```lean
lemma smul_def (r : R) (p : CMvPolynomial n R) : r • p = C r * p
```

`CPoly.CMvPolynomial.fromCMvPolynomial_C` (lemma, [line 406](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L406))

```lean
lemma fromCMvPolynomial_C (r : R) :
    fromCMvPolynomial (C r : CMvPolynomial n R) = MvPolynomial.C r
```

`CPoly.CMvPolynomial.CHom` (definition, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L436))

> `CMvPolynomial.C` bundled as a ring homomorphism.  Computable.

```lean
def CHom : R →+* CMvPolynomial n R
```

`CPoly.CMvPolynomial.CHom_apply` (theorem, [line 451](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L451))

```lean
theorem CHom_apply (c : R) : (CHom (n := n) c) = CMvPolynomial.C c
```

`CPoly.CMvPolynomial.fromCMvPolynomial_sum` (theorem, [line 454](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L454))

> `fromCMvPolynomial` commutes with a finite sum.

```lean
theorem fromCMvPolynomial_sum {ι : Type*} (s : Finset ι) (f : ι → CMvPolynomial n R) :
    fromCMvPolynomial (∑ i ∈ s, f i) = ∑ i ∈ s, fromCMvPolynomial (f i)
```

`CPoly.CMvPolynomial.fromCMvPolynomial_prod` (theorem, [line 459](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L459))

> `fromCMvPolynomial` commutes with a finite product.

```lean
theorem fromCMvPolynomial_prod {ι : Type*} (s : Finset ι) (f : ι → CMvPolynomial n R) :
    fromCMvPolynomial (∏ i ∈ s, f i) = ∏ i ∈ s, fromCMvPolynomial (f i)
```

`CPoly.CMvPolynomial.instAlgebra` (instance, [line 463](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean#L463))

```lean
noncomputable instance instAlgebra : Algebra R (CMvPolynomial n R)
```

## Depends on

- [`CMvPolynomial`/`MvPolynomial` Core](core.md)

## Sources

- [CompPoly/Multivariate/MvPolyEquiv/Instances.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multivariate/MvPolyEquiv/Instances.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Multivariate.MvPolyEquiv.Instances.json)
