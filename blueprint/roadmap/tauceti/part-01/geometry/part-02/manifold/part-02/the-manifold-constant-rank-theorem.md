---
declaration: theorem
origin: cited
lean: ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp
statement: formalized
proof: formalized
---

# The manifold constant rank theorem

A `C^n` map, `1 ≤ n`, whose rank on an open
neighbourhood does not exceed its rank at the centre is its derivative in suitable `C^n` local
coordinates centred at zero. The coordinate neighbourhood lies inside the prescribed open set.
No separation or countability hypotheses on the manifolds are required.

```lean
ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp.{u_1, u_2, u_3, u_4, u_5, u_6, u_7}
  {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3} {H : Type u_4} {G : Type u_5} {M : Type u_6}
  {N : Type u_7} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace F] [TopologicalSpace H]
  [TopologicalSpace G] {I : ModelWithCorners 𝕜 E H} [I.Boundaryless] {J : ModelWithCorners 𝕜 F G}
  [J.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] [TopologicalSpace N] [ChartedSpace G N]
  {n : WithTop ℕ∞} [IsManifold I n M] [IsManifold J n N] {f : M → N} {U : Set M} {x : M}
  (hf : ContMDiffOn I J n f U) (hU : IsOpen U) (hx : x ∈ U) (hn : 1 ≤ n)
  (hrank : ∀ y ∈ U, TauCeti.mfderivRank I J f y ≤ TauCeti.mfderivRank I J f x) :
  ∃ φ ψ,
    x ∈ φ.source ∧
      φ.source ⊆ U ∧
        ↑φ x = 0 ∧
          ContMDiffOn I (modelWithCornersSelf 𝕜 E) n (↑φ) φ.source ∧
            ContMDiffOn (modelWithCornersSelf 𝕜 E) I n (↑φ.symm) φ.target ∧
              ↑ψ (f x) = 0 ∧
                ContMDiffOn J (modelWithCornersSelf 𝕜 F) n (↑ψ) ψ.source ∧
                  ContMDiffOn (modelWithCornersSelf 𝕜 F) J n (↑ψ.symm) ψ.target ∧
                    Set.MapsTo f φ.source ψ.source ∧
                      ∀ y ∈ φ.source,
                        ↑ψ (f y) =
                          (tangentSpaceCastModel J (f x))
                            ((mfderiv% f x) ((tangentSpaceCastModel I x).symm (↑φ y)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The constant rank theorem](../../../../analysis/part-02/calculus/part-01/the-constant-rank-theorem.md)

## Lean

Formalized in Tau Ceti as [`ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ConstantRank.html#ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp).

## Sources

- [Tau Ceti documentation: `ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/ConstantRank.html#ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp)
- [Source of `ContMDiffOn.exists_openPartialHomeomorph_comp_eq_mfderiv_comp` in TauCeti/Geometry/Manifold/ConstantRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/ConstantRank.lean#L54)
