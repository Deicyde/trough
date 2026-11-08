---
declaration: theorem
origin: cited
lean: TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul
statement: formalized
proof: formalized
---

# The Evens norm of a Kummer class over a local field, as an element of `H²(G_K, 𝔽₂)`

if
`L` is generated over a local field `K` by a square root `x ∉ K` of `d`, and `a ∈ Lˣ` has nonzero
trace `t`, then `N^{Ev}((a)) = ε((t, −d · N a)_K · (2, d)_K) • ((c) ∪ (e))` for all `c, e` with
`(c, e)_K = -1`, where `ε` sends the signs `+1`, `-1` to `0`, `1`.

```lean
TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul.{u} {K L : Type u} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Invertible 2] [Field L] [Algebra K L]
  [FiniteDimensional K L] [Invertible 2] (σ : L →ₐ[K] SeparableClosure K)
  (hfin : Module.finrank K L = 2) {x : L} {d : Kˣ} (hx : x ∉ Set.range ⇑(algebraMap K L))
  (hx2 : x ^ 2 = (algebraMap K L) ↑d) (a : Lˣ) {t : Kˣ} (ht : ↑t = (Algebra.trace K L) ↑a)
  {c e : Kˣ} (hce : TauCeti.hilbertSymbol c e = -1) :
  TauCeti.galoisEvens K L σ hfin (TauCeti.kummerClass a) =
    TauCeti.additiveIntUnitsAddEquiv
        (Additive.ofMul
          (TauCeti.hilbertSymbol t (-(d * (TauCeti.Algebra.normUnits K) a)) *
            TauCeti.hilbertSymbol (unitOfInvertible 2) d)) •
      (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1)
          (TauCeti.kummerClass c))
        (TauCeti.kummerClass e)
```

## Depends on

- [The index-two degree-one Evens norm `Nᴱᵛ : H¹(U, 𝔽₂) → H²(G, 𝔽₂)` for an open subgroup `U` of index two](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-index-two-degree-one-evens-norm-nev-h1-u-f2.md)

## Proof depends on

- [A Kummer cup over a local field is its Hilbert symbol times a fixed nonzero cup](a-kummer-cup-over-a-local-field-is-its-hilbert-s.md)
- [The comparison isomorphism `Br(K) ≃ H²_cont(G_K, (Kˢ)ˣ)` with Mathlib's continuous cohomology, for `K` in any universe](the-comparison-isomorphism-br-k-h2-cont-g-k-ks-x.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [Serre's formula for the Evens norm of a Kummer class (Serre, Théorème 1′ at `n = 2`)](../../../field-theory/other-results/serres-formula-for-the-evens-norm-of-a-kummer-cl.md)
- [The Skolem-Noether theorem](../../../algebra/central-simple/the-skolem-noether-theorem.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](the-splitting-criterion-for-quaternion-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul)
- [Source of `TauCeti.galoisEvens_kummerClass_eq_hilbertSymbol_smul` in TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.lean#L163)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
