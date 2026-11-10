---
declaration: section
origin: cited
lean: Stacks.Cohomology.CechBoundary.exists_covering_localLifts, Stacks.Cohomology.CechBoundary.exists_cocycle_of_localLifts, Stacks.Cohomology.CechBoundary.cls_eq_of_localLifts, Stacks.Cohomology.CechBoundary.cls_add_of_localLifts, Stacks.Cohomology.CechBoundary.cls_eq_of_refinement_of_localLifts, Stacks.Cohomology.CechBoundary.exists_common_refinement_cls_eq_of_localLifts
statement: formalized
proof: formalized
---

# 111.41 Čech Cohomology

Section 111.41 of the Stacks Project, [Tag 02AO](https://stacks.math.columbia.edu/tag/02AO). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02AP, a definition

[Tag 02AP](https://stacks.math.columbia.edu/tag/02AP) in the Stacks Project.

**`Stacks.Cohomology.CechBoundary.exists_covering_localLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean#L109). The attribute's comment: “existence of a covering with lifts”.

> If `ψ : ℱ₂ ⟶ ℱ₃` is locally surjective for the topology of open covers, then every section `τ`
> of `ℱ₃` over an open `W` admits an open covering of `W` together with a `0`-cochain of `ℱ₂`
> lifting the restrictions of `τ`.

```lean
theorem exists_covering_localLifts {W : Opens X} (τ : ToType (ℱ₃.obj (op W)))
    (hψ : CategoryTheory.Presheaf.IsLocallySurjective (Opens.grothendieckTopology X) ψ) :
    ∃ (I₀ : Type uX) (U₀ : I₀ → Opens X) (hU₀ : W = ⨆ i, U₀ i) (lift : Cochain U₀ ℱ₂ 0),
      ∀ i : Fin 1 → I₀,
        ψ.app (op (inter U₀ i)) (lift i) = restr ℱ₃ (inter_le_of_eq_iSup hU₀ i) τ
```

**`Stacks.Cohomology.CechBoundary.exists_cocycle_of_localLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean#L139). The attribute's comment: “the cocycle”.

> Let `φ : ℱ₁ ⟶ ℱ₂` be injective on sections and `ℱ₁ → ℱ₂ → ℱ₃` exact in the middle on
> sections. If `τ` is a section of `ℱ₃` over `W` and `lift` is a `0`-cochain of `ℱ₂` lifting the
> restrictions of `τ`, then the coboundary of `lift` is the image of a `1`-cocycle of `ℱ₁`.

```lean
theorem exists_cocycle_of_localLifts
    (hmono : ∀ V : Opens X, Function.Injective (φ.app (op V)))
    (hexact : ∀ (V : Opens X) (b : ToType (ℱ₂.obj (op V))), ψ.app (op V) b = 0 →
      ∃ a, φ.app (op V) a = b)
    (hlift : ∀ i, ψ.app (op (inter U i)) (lift i) = restr ℱ₃ (hle i) τ) :
    ∃ c : cocycles1 U ℱ₁, push U φ 1 (c : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift
```

**`Stacks.Cohomology.CechBoundary.cls_eq_of_localLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean#L162). The attribute's comment: “well-definedness in the lifts”.

> Let `φ : ℱ₁ ⟶ ℱ₂` be injective on sections and `ℱ₁ → ℱ₂ → ℱ₃` exact in the middle on
> sections. Two systems of lifts of the same section give `1`-cocycles of `ℱ₁` with the same class
> in `Ȟ¹(𝒰, ℱ₁)`.

```lean
theorem cls_eq_of_localLifts
    (hmono : ∀ V : Opens X, Function.Injective (φ.app (op V)))
    (hexact : ∀ (V : Opens X) (b : ToType (ℱ₂.obj (op V))), ψ.app (op V) b = 0 →
      ∃ a, φ.app (op V) a = b)
    {lift' : Cochain U ℱ₂ 0}
    (hlift : ∀ i, ψ.app (op (inter U i)) (lift i) = restr ℱ₃ (hle i) τ)
    (hlift' : ∀ i, ψ.app (op (inter U i)) (lift' i) = restr ℱ₃ (hle i) τ)
    {c c' : cocycles1 U ℱ₁}
    (hc : push U φ 1 (c : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift)
    (hc' : push U φ 1 (c' : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift') :
    cls U ℱ₁ c = cls U ℱ₁ c'
```

**`Stacks.Cohomology.CechBoundary.cls_add_of_localLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean#L190). The attribute's comment: “additivity of the boundary map”.

> Let `φ : ℱ₁ ⟶ ℱ₂` be injective on sections. The class attached to the sum of two systems of
> local lifts is the sum of the two classes.

```lean
theorem cls_add_of_localLifts
    (hmono : ∀ V : Opens X, Function.Injective (φ.app (op V)))
    {lift' : Cochain U ℱ₂ 0} {c c' d : cocycles1 U ℱ₁}
    (hc : push U φ 1 (c : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift)
    (hc' : push U φ 1 (c' : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift')
    (hd : push U φ 1 (d : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 (lift + lift')) :
    cls U ℱ₁ d = cls U ℱ₁ c + cls U ℱ₁ c'
```

**`Stacks.Cohomology.CechBoundary.cls_eq_of_refinement_of_localLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean#L221). The attribute's comment: “independence of the covering, on a given common refinement”.

> Let `φ : ℱ₁ ⟶ ℱ₂` be injective on sections and `ℱ₁ → ℱ₂ → ℱ₃` exact in the middle on
> sections. Let `𝒰` and `𝒰'` be two families of opens over `W`, each carrying a system of lifts of
> the same section `τ` of `ℱ₃`, and let `𝒱` be a common refinement of the two: a family of opens
> with refinement functions into the index sets of `𝒰` and of `𝒰'`. Then the two classes attached
> to `τ` have the same image in `Ȟ¹(𝒱, ℱ₁)`.

```lean
theorem cls_eq_of_refinement_of_localLifts
    (U' : I' → Opens X) (V : K → Opens X)
    (r : K → I) (hr : ∀ k, V k ≤ U (r k))
    (r' : K → I') (hr' : ∀ k, V k ≤ U' (r' k))
    (hle' : ∀ i : Fin 1 → I', inter U' i ≤ W)
    (hmono : ∀ V₀ : Opens X, Function.Injective (φ.app (op V₀)))
    (hexact : ∀ (V₀ : Opens X) (b : ToType (ℱ₂.obj (op V₀))), ψ.app (op V₀) b = 0 →
      ∃ a, φ.app (op V₀) a = b)
    {lift' : Cochain U' ℱ₂ 0}
    (hlift : ∀ i, ψ.app (op (inter U i)) (lift i) = restr ℱ₃ (hle i) τ)
    (hlift' : ∀ i, ψ.app (op (inter U' i)) (lift' i) = restr ℱ₃ (hle' i) τ)
    {c : cocycles1 U ℱ₁} {c' : cocycles1 U' ℱ₁}
    (hc : push U φ 1 (c : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift)
    (hc' : push U' φ 1 (c' : Cochain U' ℱ₁ 1) = cechD U' ℱ₂ 0 lift') :
    refinementCechH1 U V r hr ℱ₁ (cls U ℱ₁ c) =
      refinementCechH1 U' V r' hr' ℱ₁ (cls U' ℱ₁ c')
```

**`Stacks.Cohomology.CechBoundary.exists_common_refinement_cls_eq_of_localLifts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CechToCohomology/BoundaryCocycle.lean#L263). The attribute's comment: “independence of the covering”.

> Let `φ : ℱ₁ ⟶ ℱ₂` be injective on sections and `ℱ₁ → ℱ₂ → ℱ₃` exact in the middle on
> sections. Two families of opens covering `W`, each carrying a system of lifts of the same section
> `τ` of `ℱ₃`, admit a common refinement covering `W`, the family of their pairwise intersections,
> on which the two classes attached to `τ` agree.

```lean
theorem exists_common_refinement_cls_eq_of_localLifts
    (U' : I' → Opens X) (hU : W = ⨆ i, U i) (hU' : W = ⨆ i', U' i')
    (hmono : ∀ V₀ : Opens X, Function.Injective (φ.app (op V₀)))
    (hexact : ∀ (V₀ : Opens X) (b : ToType (ℱ₂.obj (op V₀))), ψ.app (op V₀) b = 0 →
      ∃ a, φ.app (op V₀) a = b)
    {lift' : Cochain U' ℱ₂ 0}
    (hlift : ∀ i, ψ.app (op (inter U i)) (lift i) = restr ℱ₃ (inter_le_of_eq_iSup hU i) τ)
    (hlift' : ∀ i, ψ.app (op (inter U' i)) (lift' i) = restr ℱ₃ (inter_le_of_eq_iSup hU' i) τ)
    {c : cocycles1 U ℱ₁} {c' : cocycles1 U' ℱ₁}
    (hc : push U φ 1 (c : Cochain U ℱ₁ 1) = cechD U ℱ₂ 0 lift)
    (hc' : push U' φ 1 (c' : Cochain U' ℱ₁ 1) = cechD U' ℱ₂ 0 lift') :
    ∃ (V : I × I' → Opens X) (r : I × I' → I) (hr : ∀ k, V k ≤ U (r k))
      (r' : I × I' → I') (hr' : ∀ k, V k ≤ U' (r' k)),
      W = ⨆ k, V k ∧
        refinementCechH1 U V r hr ℱ₁ (cls U ℱ₁ c) =
          refinementCechH1 U' V r' hr' ℱ₁ (cls U' ℱ₁ c')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.41, Tag 02AO](https://stacks.math.columbia.edu/tag/02AO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
