---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.GroupOverField.isRepresentable_relocalizeRestrict_algebraicClosure_of_isSeparatedOver, AlgebraicGeometry.Space.GroupOverField.isRepresentable_of_isSeparatedOver_of_isLocallyOfFiniteType, AlgebraicGeometry.Space.GroupOverField.isRepresentable_of_isSeparatedOver
statement: formalized
proof: formalized
---

# 79.10 Group algebraic spaces over fields

Section 79.10 of the Stacks Project, [Tag 0B8D](https://stacks.math.columbia.edu/tag/0B8D). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B8E, a lemma

[Tag 0B8E](https://stacks.math.columbia.edu/tag/0B8E) in the Stacks Project.

**`AlgebraicGeometry.Space.GroupOverField.isRepresentable_relocalizeRestrict_algebraicClosure_of_isSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpacesOverFields/AlgebraicClosureScheme.lean, line 662](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpacesOverFields/AlgebraicClosureScheme.lean#L662).

> Let `k` be a field with algebraic closure `k̄` and let `G` be a separated group algebraic
> space over `k`. Then `G_{k̄}` is a scheme.
>
> By `AlgebraicGeometry.Space.GroupOverField.exists_isAlgClosed_isRepresentable_relocalizeRestrict`
> the base change `G_L` is a scheme for some algebraically closed extension `L/k`; this is the
> source's argument with translations of the group and Jacobson charts. A separated algebraic space
> over the affine `Spec k` is quasi-separated, so Stacks 0B84 part (1) descends this to `k̄`.

```lean
theorem isRepresentable_relocalizeRestrict_algebraicClosure_of_isSeparatedOver
    (B : BigFppfSite.{u}) (hk : B.Contains (Spec (.of k)))
    (G : GroupAlgebraicSpace B (Spec (.of k)) hk (yoneda.obj (⊤_ (BigFppfOver B (Spec (.of k)) hk)))
      (isAlgebraicSpace_yoneda B (Spec (.of k)) hk _))
    (hsep : IsSeparatedOver B (Spec (.of k)) hk G.obj.X.left) :
    ((OverShriek.relocalizeRestrict (specExtensionHom k (AlgebraicClosure k) B hk
      (contains_spec_of_isAlgebraic B k (AlgebraicClosure k) hk))).obj
        G.obj.X.left).IsRepresentable
```

## Tag 0B8F, a lemma

[Tag 0B8F](https://stacks.math.columbia.edu/tag/0B8F) in the Stacks Project.

**`AlgebraicGeometry.Space.GroupOverField.isRepresentable_of_isSeparatedOver_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpacesOverFields/SeparatedFiniteTypeScheme.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpacesOverFields/SeparatedFiniteTypeScheme.lean#L50).

> **A separated group algebraic space locally of finite type over a field is a scheme.** Let
> `G` be a group algebraic space over `S ≅ Spec k` which is separated over `k` and locally of
> finite type over `k`. Then `G` is representable.
>
> Being separated over `k`, the space `G` is locally separated over `k`, hence decent, and a decent
> group algebraic space locally of finite type over a field is a scheme.

```lean
theorem isRepresentable_of_isSeparatedOver_of_isLocallyOfFiniteType (e : S ≅ Spec (.of k))
    (G : GroupAlgebraicSpace C S hS (yoneda.obj (⊤_ (BigFppfOver C S hS)))
      (isAlgebraicSpace_yoneda C S hS _))
    (hsep : IsSeparatedOver C S hS G.obj.X.left)
    (hlft : IsLocallyOfFiniteType C S hS
      ((isTerminal_yoneda_obj_base C S hS).from G.obj.X.left)) :
    G.obj.X.left.IsRepresentable
```

## Tag 0B8G, a proposition

[Tag 0B8G](https://stacks.math.columbia.edu/tag/0B8G) in the Stacks Project.

**`AlgebraicGeometry.Space.GroupOverField.isRepresentable_of_isSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpacesOverFields/SeparatedScheme.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupSpacesOverFields/SeparatedScheme.lean#L253).

> **Stacks 0B8G.** Let `k` be a field and let `G` be a group algebraic space over `k`. If `G`
> is separated, then `G` is a scheme.
>
> By Stacks 0B8E the base change `G_{k̄}` is a scheme `X₀`. For a purely transcendental extension
> `K = k(x_σ)` of cardinality above the size of `X₀`, Stacks 0B85 reduces the statement to `G_K`.
> With `Ω` the algebraic closure of `K`, the base change `G_Ω = X₀ ×_{k̄} Ω` is a Jacobson scheme
> whose closed points are `Ω`-rational (Stacks 0479), and
> `AlgebraicGeometry.Space.GroupOverField.isRepresentable_of_relocalizeRestrict_algebraicClosure`
> concludes that `G_K` is a scheme.

```lean
theorem isRepresentable_of_isSeparatedOver {k : Type u} [Field k] (B : BigFppfSite.{u})
    (hk : B.Contains (Spec (.of k)))
    (G : GroupAlgebraicSpace B (Spec (.of k)) hk (yoneda.obj (⊤_ (BigFppfOver B (Spec (.of k)) hk)))
      (isAlgebraicSpace_yoneda B (Spec (.of k)) hk _))
    (hsep : IsSeparatedOver B (Spec (.of k)) hk G.obj.X.left) :
    G.obj.X.left.IsRepresentable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.10, Tag 0B8D](https://stacks.math.columbia.edu/tag/0B8D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
