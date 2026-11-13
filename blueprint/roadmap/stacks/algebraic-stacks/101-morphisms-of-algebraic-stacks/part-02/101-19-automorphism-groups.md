---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isRepresentable_pointAutomorphismSpace, AlgebraicGeometry.Stack.exists_pointAutomorphismSpace_iff_forall, AlgebraicGeometry.Stack.AutomorphismGroupHasProperty, AlgebraicGeometry.Stack.automorphismGroupHasProperty_iff_of_representative, AlgebraicGeometry.Stack.inducesIsomorphismAt_iff_forall_representatives, AlgebraicGeometry.Stack.exists_isIso_pointAutomorphismSpaceMap_iff_forall, AlgebraicGeometry.Stack.InducesIsomorphismAt
statement: formalized
proof: formalized
---

# 101.19 Automorphism groups

Section 101.19 of the Stacks Project, [Tag 0DTR](https://stacks.math.columbia.edu/tag/0DTR). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DTS, a lemma

[Tag 0DTS](https://stacks.math.columbia.edu/tag/0DTS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentable_pointAutomorphismSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupScheme.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupScheme.lean#L83). The attribute's comment: “the automorphism group algebraic space of a field-valued point is a scheme under any of the six conditions”.

> **Stacks 0DTS.** Let `𝒳` be an algebraic stack over `S` and let `x : Spec k ⟶ 𝒳` be a
> field-valued point with automorphism group algebraic space `G_x = Isom_𝒳(x, x)` over `Spec k`.
> Then `G_x` is a scheme if one of the following holds: the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` is
> quasi-separated, `Δ` is locally separated, `𝒳` is quasi-DM, the inertia projection
> `I_𝒳 ⟶ 𝒳` is quasi-separated, `I_𝒳 ⟶ 𝒳` is locally separated, or `I_𝒳 ⟶ 𝒳` is locally
> quasi-finite.
>
> Products are over `S` (Properties of Stacks, Section 04XA), the properties of `Δ` and of
> `I_𝒳 ⟶ 𝒳` are taken in the sense of Properties of Stacks, Section 04XB, quasi-DM is the absolute
> notion of Stacks 050D (over `Spec ℤ`), and "is a scheme" is representability of the presheaf
> `G_x` on the big fppf site of `Spec k`.

```lean
theorem isRepresentable_pointAutomorphismSpace (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (x : FieldValuedPoint B S hS 𝒳.val.val)
    (h : IsQuasiSeparated B S hS (diagonal.{u, u, u + 1} B S hS 𝒳.val) ∨
      IsLocallySeparated B S hS (diagonal.{u, u, u + 1} B S hS 𝒳.val) ∨
      AlgebraicStacks.IsAbsolutelyQuasiDM B S hS B.contains_terminal 𝒳 ∨
      IsQuasiSeparated B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳).hom ∨
      IsLocallySeparated B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳).hom ∨
      IsLocallyQuasiFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳).hom) :
    (pointAutomorphismSpace B S hS 𝒳.val x).IsRepresentable
```

## Tag 0DTT, a lemma

[Tag 0DTT](https://stacks.math.columbia.edu/tag/0DTT) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_pointAutomorphismSpace_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupGroundFieldExtension.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupGroundFieldExtension.lean#L531).

> **Stacks 0DTT.** Let `𝒳` be an algebraic stack, let `q ∈ |𝒳|` be a point and let `P` be a
> property of algebraic spaces over fields which is invariant under ground field extensions. Then
> the automorphism group algebraic space `G_x/k` has `P` for *some* field-valued representative
> `x : Spec k → 𝒳` of `q` if and only if it has `P` for *every* field-valued representative.

```lean
theorem exists_pointAutomorphismSpace_iff_forall
    (q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids)
    (P : ∀ U : BigFppfOver B S hS, ((BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u) → Prop)
    (hP : IsInvariantUnderGroundFieldExtension B S hS P) :
    (∃ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = q ∧
        P p.base (pointAutomorphismSpace B S hS 𝒳.val p)) ↔
      ∀ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = q →
        P p.base (pointAutomorphismSpace B S hS 𝒳.val p)
```

## Tag 0DTU, a remark

[Tag 0DTU](https://stacks.math.columbia.edu/tag/0DTU) in the Stacks Project.

**`AlgebraicGeometry.Stack.AutomorphismGroupHasProperty`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupProperty.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupProperty.lean#L105). The attribute's comment: “the definition: the automorphism group of a stack at a point has P when the automorphism group algebraic space of every field-valued representative has P”.

> **Stacks 0DTU.** Let `P` be a property of algebraic spaces over fields and let `q` be a point
> of `|𝒳|` for an algebraic stack `𝒳`. The *automorphism group of `𝒳` at `q` has `P`* when the
> automorphism group algebraic space `G_x/k = Isom_𝒳(x, x)` has `P` for every field-valued
> representative `x : Spec k → 𝒳` of `q`.
>
> This is condition (2) of Stacks 0DTT, so it makes no choice of representative. When `P` is
> invariant under ground field extensions
> (`AlgebraicGeometry.Stack.IsInvariantUnderGroundFieldExtension`) it agrees with condition (1) of
> Stacks 0DTT by `AlgebraicGeometry.Stack.automorphismGroupHasProperty_iff_exists`, and it is
> decided by any single representative by
> `AlgebraicGeometry.Stack.automorphismGroupHasProperty_iff_of_representative`; that is what makes
> the phrase well posed, and it is the content of Remark 0DTU.

```lean
def AutomorphismGroupHasProperty
    (P : ∀ U : BigFppfOver B S hS, ((BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u) → Prop)
    (q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids) : Prop
```

**`AlgebraicGeometry.Stack.automorphismGroupHasProperty_iff_of_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupProperty.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupProperty.lean#L148). The attribute's comment: “the phrase is well posed: for a property invariant under ground field extensions, an arbitrary single field-valued representative decides it”.

> **Stacks 0DTU: the phrase is well posed.** For a property `P` of algebraic spaces over fields
> which is invariant under ground field extensions, the statement that the automorphism group of
> `𝒳` at `q` has `P` is decided by an arbitrary single field-valued representative `p` of `q`:
> it holds exactly when the automorphism group algebraic space `G_p` has `P`. In particular the
> answer does not depend on which representative of `q` one reads it at, which is what licenses
> the phrase "the automorphism group of `𝒳` at `q` has `P`" of Remark 0DTU.

```lean
theorem automorphismGroupHasProperty_iff_of_representative
    (P : ∀ U : BigFppfOver B S hS, ((BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u) → Prop)
    (hP : IsInvariantUnderGroundFieldExtension B S hS P)
    {q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids}
    (p : FieldValuedPoint B S hS 𝒳.val.val)
    (hp : pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = q) :
    AutomorphismGroupHasProperty B S hS P q ↔
      P p.base (pointAutomorphismSpace B S hS 𝒳.val p)
```

## Tag 0DTV, a lemma

[Tag 0DTV](https://stacks.math.columbia.edu/tag/0DTV) in the Stacks Project.

**`AlgebraicGeometry.Stack.inducesIsomorphismAt_iff_forall_representatives`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupAtPoint.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupAtPoint.lean#L326). The attribute's comment: “for the lifts of one field-valued representative: some lift, hence any lift”.

> A 1-morphism of algebraic stacks induces an isomorphism between automorphism groups at a
> point of `|𝒳|` exactly when it does so at *every* object lying above *every* field-valued
> representative of that point: one pullback of one representative above each object of the big
> site already decides it, because in a category fibred in groupoids any two lifts of the same
> morphism of the base are isomorphic over an identity.
>
> This is Stacks 0DTV for the lifts of one field-valued representative. Passing between two
> representatives of the same point is a descent statement, proved for the automorphism group
> algebraic spaces in
> `AlgebraicGeometry.Stack.exists_isIso_pointAutomorphismSpaceMap_iff_forall`: the map of
> automorphism group algebraic spaces over a field extension is a base change, and being an
> isomorphism is fpqc local on the target (Stacks 041Y).
> `AlgebraicGeometry.Stack.InducesIsomorphismAt` quantifies over *all* field-valued
> representatives, which is condition (2) of Stacks 0DTV and so never weaker than the notion of
> Stacks 0DTW.

```lean
theorem inducesIsomorphismAt_iff_forall_representatives (f : 𝒳 ⟶ 𝒴)
    (q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids) :
    InducesIsomorphismAt B S hS f q ↔
      ∀ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = q →
          InducesIsomorphismAtObject B S hS f p.obj
```

**`AlgebraicGeometry.Stack.exists_isIso_pointAutomorphismSpaceMap_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupGroundFieldExtension.lean, line 698](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupGroundFieldExtension.lean#L698).

> **Stacks 0DTV.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks and let `x` be a point
> of `|𝒳|`. The map `G_x ⟶ G_y` of automorphism group algebraic spaces, where `y = f ∘ x`, is an
> isomorphism for *some* field-valued representative `x : Spec k → 𝒳` of the point if and only if
> it is an isomorphism for *every* such representative.
>
> Two representatives of one point admit a common refinement. Over a field extension the map of
> automorphism group algebraic spaces is a base change of the map below, and being an isomorphism
> is fpqc local on the target (**Stacks 041Y**), so it passes both ways between a representative
> and a refinement.

```lean
theorem exists_isIso_pointAutomorphismSpaceMap_iff_forall (f : 𝒳 ⟶ 𝒴)
    (q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids) :
    (∃ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = q ∧
          IsIso (pointAutomorphismSpaceMap B S hS f p)) ↔
      ∀ p : FieldValuedPoint B S hS 𝒳.val.val,
        pointClass B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids p = q →
          IsIso (pointAutomorphismSpaceMap B S hS f p)
```

## Tag 0DTW, a remark

[Tag 0DTW](https://stacks.math.columbia.edu/tag/0DTW) in the Stacks Project.

**`AlgebraicGeometry.Stack.InducesIsomorphismAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupAtPoint.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AutomorphismGroupAtPoint.lean#L280). The attribute's comment: “f induces an isomorphism between automorphism groups at a point”.

> A 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks *induces an isomorphism between automorphism
> groups at a point* `q` of `|𝒳|` and at `f(q)` — in the literature, `f` is *stabilizer
> preserving*, or *fixed-point reflecting*, at `q` — when for every field-valued representative `p`
> of `q` and every object of the big site the morphism of automorphism group algebraic spaces of
> `p` has a pullback of `p` at which it is bijective on sections.
>
> By `AlgebraicGeometry.Stack.inducesIsomorphismAt_iff_forall_representatives` one such pullback
> per object of the site is enough: the condition then holds at every object lying above every
> representative of `q`, which is the content of Stacks 0DTV for the representatives of a fixed
> field-valued point.

```lean
def InducesIsomorphismAt (f : 𝒳 ⟶ 𝒴)
    (q : points B S hS 𝒳.val.val 𝒳.val.isFiberedInGroupoids) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.19, Tag 0DTR](https://stacks.math.columbia.edu/tag/0DTR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
