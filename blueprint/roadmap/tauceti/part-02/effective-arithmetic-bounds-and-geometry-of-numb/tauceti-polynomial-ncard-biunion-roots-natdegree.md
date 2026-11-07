---
declaration: theorem
origin: cited
lean: TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le
statement: formalized
proof: formalized
---

# TauCeti.Polynomial.ncard\_biUnion\_roots\_natDegree\_le\_abs\_intCoeff\_le

The integer specialisation: the roots in a domain `S` of all integer polynomials of degree at
most `d` with every coefficient bounded by `B` in absolute value number at most
`(2 · B + 1) ^ (d + 1) · d`. Each of the `2 · B + 1` integers in `[-B, B]` is an allowed
coefficient, and a degree-`≤ d` polynomial has at most `d` roots.

```lean
TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le.{u_2} {S : Type u_2}
  [CommRing S] [IsDomain S] [DecidableEq S] (m : ℤ →+* S) (d B : ℕ) :
  (⋃ f,
        ⋃ (_ : f.natDegree ≤ d ∧ ∀ (i : ℕ), |f.coeff i| ≤ ↑B),
          ↑(Polynomial.map m f).roots.toFinset).ncard ≤
    (2 * B + 1) ^ (d + 1) * d
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Card/RootSetUnion.html#TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Card/RootSetUnion.html#TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le)
- [Source of `TauCeti.Polynomial.ncard_biUnion_roots_natDegree_le_abs_intCoeff_le` in TauCeti/Algebra/Polynomial/Card/RootSetUnion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Polynomial/Card/RootSetUnion.lean#L101)
- [Tau Ceti roadmap status: Effective arithmetic bounds and geometry of numbers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/EffectiveBounds/STATUS.md)
