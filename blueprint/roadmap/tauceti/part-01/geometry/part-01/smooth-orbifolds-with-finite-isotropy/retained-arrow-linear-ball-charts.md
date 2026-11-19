---
declaration: theorem
origin: cited
lean: TauCeti.exists_linear_ball_isotropy_chart
statement: formalized
proof: formalized
---

# Retained-arrow linear-ball charts

Every object of a proper étale real groupoid has,
inside any prescribed neighbourhood, a fully faithful linear-ball action chart of its full
finite isotropy group. The object and labelled-arrow maps are open embeddings and local
`C^n` diffeomorphisms. At the origin the arrow labelled `g` is the original arrow `g`,
including ineffective isotropy. The squared radius is measured with the orbit-sum inner
product.

```lean
TauCeti.exists_linear_ball_isotropy_chart.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  {H : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {E' : Type u_3} {H' : Type u_4}
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  {n : WithTop ℕ∞} {C : Type u_5} [CategoryTheory.Groupoid C] [TopologicalSpace C]
  [ChartedSpace H C] [IsManifold I n C] [TopologicalSpace (Quiver.Total C)]
  [ChartedSpace H' (Quiver.Total C)] [T2Space (Quiver.Total C)]
  (hp : IsProperMap fun a => (a.left, a.right)) (hs : IsLocalDiffeomorph J I n Quiver.Total.left)
  (ht : IsLocalDiffeomorph J I n Quiver.Total.right)
  (hu : Continuous fun y => { left := y, right := y, hom := CategoryTheory.CategoryStruct.id y })
  (hc : Continuous fun p => (↑p).1.comp (↑p).2 ⋯) (hn : 1 ≤ n) (x : C) {s : Set C}
  (hsx : s ∈ nhds x) :
  ∃ ι σ c B x_1 f z F,
    0 < c ∧
      ↑B =
          (ContRepresentation.toRepresentation ℝ (CategoryTheory.Aut x) E
                σ).sumOfConjugatesInnerSublevel
            c ∧
        ↑z = 0 ∧
          f z = x ∧
            (∀ (g : CategoryTheory.Aut x) (v : ↥B), ↑(g • v) = (σ g) ↑v) ∧
              ContMDiffConstSMul (modelWithCornersSelf ℝ E) n (CategoryTheory.Aut x) ↥B ∧
                Topology.IsOpenEmbedding f ∧
                  IsLocalDiffeomorph (modelWithCornersSelf ℝ E) I n f ∧
                    Set.range f ⊆ s ∧
                      (∀ (a : CategoryTheory.ActionCategory (CategoryTheory.Aut x) ↥B),
                          F.obj a = f a.back) ∧
                        F.Full ∧
                          F.Faithful ∧
                            (∀ (g : CategoryTheory.Aut x),
                                Topology.IsOpenEmbedding fun v =>
                                  {
                                    left :=
                                      F.obj
                                        ((CategoryTheory.ActionCategory.totalEquiv
                                                (CategoryTheory.Aut x) ↥B).symm
                                            (g, v)).left,
                                    right :=
                                      F.obj
                                        ((CategoryTheory.ActionCategory.totalEquiv
                                                (CategoryTheory.Aut x) ↥B).symm
                                            (g, v)).right,
                                    hom :=
                                      F.map
                                        ((CategoryTheory.ActionCategory.totalEquiv
                                                (CategoryTheory.Aut x) ↥B).symm
                                            (g, v)).hom }) ∧
                              (∀ (g : CategoryTheory.Aut x),
                                  IsLocalDiffeomorph (modelWithCornersSelf ℝ E) J n fun v =>
                                    {
                                      left :=
                                        F.obj
                                          ((CategoryTheory.ActionCategory.totalEquiv
                                                  (CategoryTheory.Aut x) ↥B).symm
                                              (g, v)).left,
                                      right :=
                                        F.obj
                                          ((CategoryTheory.ActionCategory.totalEquiv
                                                  (CategoryTheory.Aut x) ↥B).symm
                                              (g, v)).right,
                                      hom :=
                                        F.map
                                          ((CategoryTheory.ActionCategory.totalEquiv
                                                  (CategoryTheory.Aut x) ↥B).symm
                                              (g, v)).hom }) ∧
                                ∀ (g : CategoryTheory.Aut x),
                                  {
                                      left :=
                                        F.obj
                                          ((CategoryTheory.ActionCategory.totalEquiv
                                                  (CategoryTheory.Aut x) ↥B).symm
                                              (g, z)).left,
                                      right :=
                                        F.obj
                                          ((CategoryTheory.ActionCategory.totalEquiv
                                                  (CategoryTheory.Aut x) ↥B).symm
                                              (g, z)).right,
                                      hom :=
                                        F.map
                                          ((CategoryTheory.ActionCategory.totalEquiv
                                                  (CategoryTheory.Aut x) ↥B).symm
                                              (g, z)).hom } =
                                    { left := x, right := x, hom := g.asIso.hom }
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for a converging family](../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_linear_ball_isotropy_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Etale/Linearization.html#TauCeti.exists_linear_ball_isotropy_chart).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_linear_ball_isotropy_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Etale/Linearization.html#TauCeti.exists_linear_ball_isotropy_chart)
- [Source of `TauCeti.exists_linear_ball_isotropy_chart` in TauCeti/Geometry/Manifold/Etale/Linearization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Etale/Linearization.lean#L48)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
