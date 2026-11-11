---
declaration: section
origin: cited
lean: AlgebraicGeometry.eq_id_of_isIso_of_eq_on_points, AlgebraicGeometry.exists_iso_pullback_of_isIso_of_eq_on_points
statement: formalized
proof: formalized
---

# 33.32 Automorphisms

Section 33.32 of the Stacks Project, [Tag 0GWY](https://stacks.math.columbia.edu/tag/0GWY). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G05, a lemma

[Tag 0G05](https://stacks.math.columbia.edu/tag/0G05) in the Stacks Project.

**`AlgebraicGeometry.eq_id_of_isIso_of_eq_on_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Automorphisms/PointwiseTrivialAut.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Automorphisms/PointwiseTrivialAut.lean#L88). The attribute's comment: “clause (2) in full: an automorphism over `k` of a reduced scheme locally of finite type over `k` fixing every point of the underlying space is the identity when every irreducible component has positive dimension. No hypothesis on the base field and nothing carried. The automorphism hypothesis is necessary — for an endomorphism the statement fails over a finite field, by `AlgHom.exists_comap_eq_ne_id_of_finite_field` — which is why this stands beside `AlgebraicGeometry.eq_id_of_eq_on_points`, the endomorphism statement with the base field in a disjunctive hypothesis”.

> **Stacks Project, Tag 0G05, clause (2).** Let `X` be a reduced scheme locally of finite type
> over a field `k` and let `f : X ⟶ X` be an automorphism over `k` which induces the identity map
> on the underlying topological space of `X`. If every irreducible component of `X` has positive
> dimension then `f` is the identity.
>
> Nothing is carried and no hypothesis is put on `k`. The source's two cases are both handled by
> the curve case `AlgebraicGeometry.eq_id_of_eq_on_points_of_isCurve`, to which
> `AlgebraicGeometry.eq_id_of_affine_curve_restrictions` reduces the statement: an integral affine
> curve over `k` is a curve in the sense of `AlgebraicGeometry.IsCurve`, being integral, separated
> and of finite type over `k` of dimension one.

```lean
theorem eq_id_of_isIso_of_eq_on_points {k : Type u} [Field k] {X : Scheme.{u}} [IsReduced X]
    (p : X ⟶ Spec (.of k)) [LocallyOfFiniteType p] (f : X ⟶ X) [IsIso f] (hf : f ≫ p = p)
    (hpoints : ∀ x : X, f x = x)
    (hdim : ∀ Z ∈ irreducibleComponents X, 0 < topologicalKrullDim Z) :
    f = 𝟙 X
```

**`AlgebraicGeometry.exists_iso_pullback_of_isIso_of_eq_on_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/Automorphisms/PointwiseTrivialAut.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/Automorphisms/PointwiseTrivialAut.lean#L232). The attribute's comment: “clause (1) in full: every module on a reduced scheme of finite type over `k` is isomorphic to its pullback along an automorphism over `k` fixing every point of the underlying space. No hypothesis on the base field, nothing carried, and the module is arbitrary rather than coherent. The connected components are clopen and finite in number; on each of them clause (2) applies, or the component is the spectrum of a finite extension of `k` and the twist of a module is isomorphic to it through a basis; the isomorphisms glue over the pairwise disjoint cover”.

> **Stacks Project, Tag 0G05, clause (1).** Let `X` be a reduced scheme of finite type over a
> field `k` and let `f : X ⟶ X` be an automorphism over `k` which induces the identity map on the
> underlying topological space of `X`. Then every `𝒪_X`-module is isomorphic to its pullback along
> `f`.
>
> Nothing is carried and no hypothesis is put on `k`; coherence of the module is not needed. The
> source's proof is "part (1) follows from part (2) and the fact that the connected components of
> `X` of dimension `0` are spectra of fields": the scheme has finitely many connected components,
> each clopen, on each of them clause (2) applies unless it is a one-point scheme, where a module
> is isomorphic to its twist through a basis, and the isomorphisms glue because the components are
> pairwise disjoint.

```lean
theorem exists_iso_pullback_of_isIso_of_eq_on_points {k : Type u} [Field k] {X : Scheme.{u}}
    (p : X ⟶ Spec (.of k))
    [LocallyOfFiniteType p] [QuasiCompact p] [IsReduced X] (f : X ⟶ X) [IsIso f]
    (hf : f ≫ p = p) (hpoints : ∀ x : X, f x = x) (F : X.Modules) :
    Nonempty ((Scheme.Modules.pullback f).obj F ≅ F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.32, Tag 0GWY](https://stacks.math.columbia.edu/tag/0GWY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
