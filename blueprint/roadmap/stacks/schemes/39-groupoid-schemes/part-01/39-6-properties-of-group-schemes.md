---
declaration: section
origin: cited
lean: AlgebraicGeometry.isSeparated_iff_isClosedImmersion_one, AlgebraicGeometry.quasiSeparated_iff_quasiCompact_one, AlgebraicGeometry.flat_mul_after_map, AlgebraicGeometry.flat_mul, AlgebraicGeometry.GroupSchemeDifferentials.relativeDifferentialsIsoPullbackIdentity, AlgebraicGeometry.GroupSchemeDifferentials.pullbackConormalIsoPullbackIdentity, AlgebraicGeometry.GroupSchemeDifferentials.relativeDifferentialsIsoPullbackConormal, AlgebraicGeometry.GroupSchemeDifferentials.exists_free_iso_relativeDifferentials_of_field
statement: formalized
proof: formalized
---

# 39.6 Properties of group schemes

Section 39.6 of the Stacks Project, [Tag 045W](https://stacks.math.columbia.edu/tag/045W). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 047G, a lemma

[Tag 047G](https://stacks.math.columbia.edu/tag/047G) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_iff_isClosedImmersion_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Separation.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Separation.lean#L88). The attribute's comment: “separated\_iff\_identity\_closed”. References: SGA 3 VIB (5.1).

> A group scheme is separated over its base if and only if its identity section is a closed
> immersion.

```lean
theorem isSeparated_iff_isClosedImmersion_one {S G : Scheme.{u}} (f : G ⟶ S)
    [GrpObj (Over.mk f)] :
    IsSeparated f ↔ IsClosedImmersion (η[Over.mk f]).left
```

**`AlgebraicGeometry.quasiSeparated_iff_quasiCompact_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Separation.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Separation.lean#L101). The attribute's comment: “quasi\_separated\_iff\_identity\_quasi\_compact”.

> A group scheme is quasi-separated over its base if and only if its identity section is
> quasi-compact.

```lean
theorem quasiSeparated_iff_quasiCompact_one {S G : Scheme.{u}} (f : G ⟶ S)
    [GrpObj (Over.mk f)] :
    QuasiSeparated f ↔ QuasiCompact η[Over.mk f].left
```

## Tag 047H, a lemma

[Tag 047H](https://stacks.math.columbia.edu/tag/047H) in the Stacks Project.

**`AlgebraicGeometry.flat_mul_after_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Flatness.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Flatness.lean#L51). The attribute's comment: “translation”.

> **Stacks Project, Tag 047H.** Left translation parametrized by a flat scheme is flat.

```lean
lemma flat_mul_after_map {S : Scheme.{u}} (G T : Over S) [GrpObj G]
    (ψ : T ⟶ G) [Flat T.hom] :
    Flat (lift (fst T G ≫ ψ) (snd T G) ≫ μ[G]).left
```

**`AlgebraicGeometry.flat_mul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Flatness.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Subgroups/Flatness.lean#L77). The attribute's comment: “multiplication”. References: SGA 3 XVIII (2.2).

> **Stacks Project, Tag 047H.** Multiplication on a flat group scheme is flat.

```lean
lemma flat_mul {S : Scheme.{u}} (G : Over S) [GrpObj G] [Flat G.hom] :
    Flat μ[G].left
```

## Tag 047I, a lemma

[Tag 047I](https://stacks.math.columbia.edu/tag/047I) in the Stacks Project.

**`AlgebraicGeometry.GroupSchemeDifferentials.relativeDifferentialsIsoPullbackIdentity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean#L149). The attribute's comment: “the composite Ω\_\{G/S} ≅ f^*e^*Ω\_\{G/S} of the chain of isomorphisms”. References: SGA 3 II (4.11.4), “(a)”.

> **The canonical isomorphism `Ω_{G/S} ≅ f^*e^*Ω_{G/S}`.**  The sheaf of relative
> differentials of a group scheme is the inverse image of its restriction along the identity
> section.

```lean
noncomputable def relativeDifferentialsIsoPullbackIdentity :
    relativeDifferentials f ≅
      (Scheme.Modules.pullback f).obj
        ((Scheme.Modules.pullback (identity f)).obj (relativeDifferentials f))
```

**`AlgebraicGeometry.GroupSchemeDifferentials.pullbackConormalIsoPullbackIdentity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean#L191). The attribute's comment: “the second isomorphism of the chain, f^*𝒞\_\{S/G} ≅ f^*e^*Ω\_\{G/S}, where 𝒞\_\{S/G} is the conormal sheaf of the identity section e: f^* of the first arrow of the conormal sequence of e, an isomorphism by Tag 0474”.

> **The second isomorphism of the chain**, `f^*𝒞_{S/G} ≅ f^*e^*Ω_{G/S}`,
> where `𝒞_{S/G}` is the conormal sheaf of the identity section `e`: the inverse image along `f`
> of `conormalIsoPullbackIdentity`, that is, of the first arrow `𝒞_{S/G} ⟶ e^*Ω_{G/S}` of the
> conormal sequence of `e`.

```lean
noncomputable def pullbackConormalIsoPullbackIdentity :
    (Scheme.Modules.pullback f).obj
        (Stacks.AlgebraicGeometry.RegularIdealSheaf.conormalSheaf (identity f) : S.Modules) ≅
      (Scheme.Modules.pullback f).obj
        ((Scheme.Modules.pullback (identity f)).obj (relativeDifferentials f))
```

**`AlgebraicGeometry.GroupSchemeDifferentials.relativeDifferentialsIsoPullbackConormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean#L203). The attribute's comment: “the first isomorphism of the chain, Ω\_\{G/S} ≅ f^*𝒞\_\{S/G}, where 𝒞\_\{S/G} is the conormal sheaf of the identity section e”.

> **The first isomorphism of the chain**, `Ω_{G/S} ≅ f^*𝒞_{S/G}`, where
> `𝒞_{S/G}` is the conormal sheaf of the identity section `e`: the shearing isomorphism
> `Ω_{G/S} ≅ f^*e^*Ω_{G/S}` followed by the inverse of `pullbackConormalIsoPullbackIdentity`.

```lean
noncomputable def relativeDifferentialsIsoPullbackConormal :
    relativeDifferentials f ≅
      (Scheme.Modules.pullback f).obj
        (Stacks.AlgebraicGeometry.RegularIdealSheaf.conormalSheaf (identity f) : S.Modules)
```

**`AlgebraicGeometry.GroupSchemeDifferentials.exists_free_iso_relativeDifferentials_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GroupScheme/Differentials.lean#L233). The attribute's comment: “freeness over a field”. References: SGA 3 II (4.11.4), “(a) over a field”.

> **Freeness over a field.**  If the base is the spectrum of a field, the sheaf of relative
> differentials of a group scheme is a free `𝒪_G`-module.

```lean
theorem exists_free_iso_relativeDifferentials_of_field (k : Type u) [Field k] (G : Scheme.{u})
    (f : G ⟶ Spec (CommRingCat.of k)) [GrpObj (Over.mk f)] :
    ∃ I : Type u,
      Nonempty (relativeDifferentials f ≅
        SheafOfModules.free (R := G.ringCatSheaf) I)
```

## Tag 0BF5, a lemma

[Tag 0BF5](https://stacks.math.columbia.edu/tag/0BF5) in the Stacks Project.

**`AlgebraicGeometry.tangentMap_mul_at_identity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/TangentIdentity.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/GroupSchemeProperties/TangentIdentity.lean#L513).

> **Stacks Project, Tag 0BF5.** The differential of group-scheme multiplication at
> the identity is addition of relative tangent vectors.

```lean
theorem tangentMap_mul_at_identity {S : Scheme.{u}} (G : Over S) [GrpObj G]
    (s : S) :
    let e : G.left := (η[G]).left s
    let m : pullback G.hom G.hom ⟶ G.left :=
      (Over.tensorObj_left G G) ▸ (μ[G]).left
    let z : ↑(pullback G.hom G.hom) :=
      (Over.tensorObj_left G G) ▸ ((lift (η[G]) (η[G])).left s)
    ∃ (h₁ : (pullback.fst G.hom G.hom) z = e)
      (h₂ : (pullback.snd G.hom G.hom) z = e)
      (hm : m z = e)
      (hbase : m ≫ G.hom = pullback.fst G.hom G.hom ≫ G.hom)
      (_ : IsIso (G.hom.residueFieldMap ((pullback.fst G.hom G.hom) z)))
      (_ : IsIso (G.hom.residueFieldMap ((pullback.snd G.hom G.hom) z)))
      (_ : IsIso (m.residueFieldMap z)),
      have : IsIso (G.hom.residueFieldMap ((pullback.fst G.hom G.hom) z)) :=
        ‹IsIso (G.hom.residueFieldMap ((pullback.fst G.hom G.hom) z))›
      have : IsIso (G.hom.residueFieldMap ((pullback.snd G.hom G.hom) z)) :=
        ‹IsIso (G.hom.residueFieldMap ((pullback.snd G.hom G.hom) z))›
      have : IsIso (m.residueFieldMap z) :=
        ‹IsIso (m.residueFieldMap z)›
      ∀ v w : DottedTangentArrow G.hom e,
        hm ▸ tangentMap m
          (pullback.fst G.hom G.hom ≫ G.hom) G.hom hbase z
          ((tangentSpaceProductEquiv G.hom G.hom z).toLinearEquiv.symm
            (h₁.symm ▸ v, h₂.symm ▸ w)) = v + w
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.6, Tag 045W](https://stacks.math.columbia.edu/tag/045W)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
