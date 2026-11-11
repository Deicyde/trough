---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma
statement: formalized
proof: formalized
---

# The relative homology across a critical level is free on the critical points

Let `f` be
a Morse function and `c` a value with a compact band `f⁻¹[c - δ, c + δ]`. For some `0 < ε ≤ δ`,
the relative singular homology `Hₙ({f ≤ c + ε}, {f ≤ c - ε}; R)`, with coefficients in an object
`R` of an abelian category with coproducts, is the coproduct of one copy of `R` for each critical
point of index `n` on the level `c`. In particular it vanishes when no critical point of the level
has index `n`.

```lean
TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma.{u, v, w, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {c δ : ℝ}
  (hf : TauCeti.IsMorse I f) (hδ : 0 < δ) (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε,
    ∃ (hε : 0 < ε),
      ε ≤ δ ∧
        ∀ {A : Type v} [inst : CategoryTheory.Category.{w, v} A] [inst_1 : CategoryTheory.Abelian A]
          [inst_2 : CategoryTheory.Limits.HasCoproducts A] (R : A) (n : ℕ),
          Nonempty ((TauCeti.sublevelPair f ⋯).singularHomology R n ≅ ∐ fun x => R)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem, in pushout form](milnors-cell-attachment-theorem-in-pushout-form.md)
- [The relative small-chain theorem](../../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Homology.html#TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Homology.html#TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma)
- [Source of `TauCeti.IsMorse.exists_singularHomology_sublevelPair_iso_sigma` in TauCeti/Geometry/Manifold/Morse/Cell/Homology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Cell/Homology.lean#L107)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
