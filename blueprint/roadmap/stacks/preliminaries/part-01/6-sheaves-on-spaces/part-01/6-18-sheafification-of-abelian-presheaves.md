---
declaration: section
origin: cited
lean: TopCat.Presheaf.piPresheaf, TopCat.Presheaf.toPiPresheaf, TopCat.Presheaf.piPresheafGerms_comp_sheafifyGerms, TopCat.Presheaf.bijective_canonicalToPullback, exists_abelian_sheafification, unique_abelian_sheafification, sheafifyAbHomEquiv
statement: formalized
proof: formalized
---

# 6.18 Sheafification of abelian presheaves

Section 6.18 of the Stacks Project, [Tag 0083](https://stacks.math.columbia.edu/tag/0083). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0084, a lemma

[Tag 0084](https://stacks.math.columbia.edu/tag/0084) in the Stacks Project.

**`TopCat.Presheaf.piPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean#L53).

> **Stacks 0084.** The product presheaf `Π(F)`: its sections over an open `U` are the families
> `(σ x)_{x ∈ U}` of germs `σ x : F.stalk x`, with restriction along `V ≤ U` given by projecting onto
> the factors indexed by the points of `V`.

```lean
noncomputable def piPresheaf (F : Presheaf (Type u) X) : Presheaf (Type u) X
```

**`TopCat.Presheaf.toPiPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean#L69).

> **Stacks 0084.** The canonical morphism of presheaves `F ⟶ Π(F)` sending a section
> `s ∈ F(U)` to the family `(s_x)_{x ∈ U}` of its germs.

```lean
noncomputable def toPiPresheaf (F : Presheaf (Type u) X) : F ⟶ piPresheaf F
```

**`TopCat.Presheaf.piPresheafGerms_comp_sheafifyGerms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean#L163).

> **Stacks 0084.** The square commutes: taking germs of a section of `F.sheafify` and then germs
> inside `Π(F)` agrees with taking germs and then pushing them forward along `F ⟶ Π(F)`.

```lean
theorem piPresheafGerms_comp_sheafifyGerms (F : Presheaf (Type u) X) (U : Opens X) :
    piPresheafGerms F U ∘ sheafifyGerms F U = piPresheafStalkMap F U ∘ sheafifyGerms F U
```

**`TopCat.Presheaf.bijective_canonicalToPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/GermFibreProduct.lean#L267).

> **Stacks 0084.** The square is a fibre-product diagram of sets: the canonical map
> `F^#(U) → Π(F)(U) ×_{∏_x Π(F)_x} ∏_x F_x` is a bijection.

```lean
theorem bijective_canonicalToPullback (F : Presheaf (Type u) X) (U : Opens X) :
    Function.Bijective (canonicalToPullback F U)
```

## Tag 0085, a lemma

[Tag 0085](https://stacks.math.columbia.edu/tag/0085) in the Stacks Project.

**`exists_abelian_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Abelian.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Abelian.lean#L176).

> **(Stacks 0085, Part 1, existence.)** A presheaf of abelian groups `F` on `X` has a
> sheafification: a sheaf of abelian groups `Fbar` with a map `F ⟶ Fbar` whose underlying map of
> presheaves of sets exhibits `Fbar` as the set-level sheafification of `F`.

```lean
theorem exists_abelian_sheafification (F : AbelianPresheafCat X) :
    ∃ (Fbar : AbelianSheafCat X) (u : F ⟶ (inclusionAbSheafToAbPresheaf X).obj Fbar)
      (iso : (forgetAbSheafToSetPresheaf X).obj Fbar ≅ setSheafifiedPresheaf X F),
      (forgetAbPresheafToSetPresheaf X).map u ≫ iso.hom =
        toSetSheafify X (underlyingSetPresheaf X F)
```

**`unique_abelian_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Abelian.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Abelian.lean#L326).

> **(Stacks 0085, Part 1, uniqueness.)**

```lean
theorem unique_abelian_sheafification
    (F : AbelianPresheafCat X)
    (Fbar₁ Fbar₂ : AbelianSheafCat X)
    (u₁ : F ⟶ (inclusionAbSheafToAbPresheaf X).obj Fbar₁)
    (u₂ : F ⟶ (inclusionAbSheafToAbPresheaf X).obj Fbar₂)
    (iso₁ : (forgetAbSheafToSetPresheaf X).obj Fbar₁ ≅ setSheafifiedPresheaf X F)
    (iso₂ : (forgetAbSheafToSetPresheaf X).obj Fbar₂ ≅ setSheafifiedPresheaf X F)
    (hu₁ : (forgetAbPresheafToSetPresheaf X).map u₁ ≫ iso₁.hom =
        toSetSheafify X (underlyingSetPresheaf X F))
    (hu₂ : (forgetAbPresheafToSetPresheaf X).map u₂ ≫ iso₂.hom =
        toSetSheafify X (underlyingSetPresheaf X F)) :
    ∃! (φ : Fbar₁ ≅ Fbar₂),
      u₁ ≫ (inclusionAbSheafToAbPresheaf X).map φ.hom = u₂ ∧
      (forgetAbSheafToSetPresheaf X).map φ.hom ≫ iso₂.hom = iso₁.hom
```

**`sheafifyAbHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Abelian.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Abelian.lean#L377). References: SGA 3 IV (4.3.16), “Hom(P, special case”.

> **(Stacks 0085, Part 2.)** The adjunction bijection
> `Hom(F^#, G) ≃ Hom(F, G)` defining sheafification of presheaves of abelian groups.

```lean
noncomputable def sheafifyAbHomEquiv (F : AbelianPresheafCat X) (G : AbelianSheafCat X) :
    ((sheafifyAb X).obj F ⟶ G) ≃ (F ⟶ (inclusionAbSheafToAbPresheaf X).obj G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.18, Tag 0083](https://stacks.math.columbia.edu/tag/0083)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
