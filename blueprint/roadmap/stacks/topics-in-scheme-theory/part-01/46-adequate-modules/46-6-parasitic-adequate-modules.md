---
declaration: section
origin: cited
lean: Stacks.Adequate.tfae_isZero_restrictModule_of_isAdequate, Stacks.Adequate.BigSite.isSerreClass_parasiticAdequate, Stacks.Adequate.BigSite.isLocalization_restrictModuleQCoh, Stacks.Adequate.isAdequate_and_isParasitic_directImage_ofAmbient
statement: formalized
proof: formalized
---

# 46.6 Parasitic adequate modules

Section 46.6 of the Stacks Project, [Tag 06ZK](https://stacks.math.columbia.edu/tag/06ZK). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06ZM, a lemma

[Tag 06ZM](https://stacks.math.columbia.edu/tag/06ZM) in the Stacks Project.

**`Stacks.Adequate.tfae_isZero_restrictModule_of_isAdequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean#L475).

> **[Stacks, Tag 06ZM].** Let `𝓕` be an adequate `𝒪`-module on a chosen big `τ`-site over
> `S`, for `τ` any of the five topologies `Zar`, `étale`, `smooth`, `syntomic`, `fppf`. The
> following are equivalent:
> 1. `v𝓕 = 0`, for the restriction `v𝓕 = 𝓕|_{S_Zar}` of `𝓕` to the small Zariski site of `S`
>    (`Stacks.Adequate.BigSite.zariskiRestrictModule`, the functor `v` of [Stacks, Tag 06VN]);
> 2. `𝓕` is parasitic;
> 3. `𝓕` is parasitic for the `τ`-topology;
> 4. `𝓕(U) = 0` for every open `U ⊆ S`;
> 5. there is an affine open covering `S = ⋃ Uᵢ` such that `𝓕(Uᵢ) = 0` for all `i`.
>
> (2)–(5) are `Stacks.Adequate.tfae_isParasitic_of_isAdequate`; (1) ⇔ (4) is the identification of
> the sections of `v𝓕` over `U` with those of `𝓕` over `U` as an object of the site.

```lean
public theorem tfae_isZero_restrictModule_of_isAdequate (B : BigSite τ S)
    (F : SheafOfModules.{u} B.structureSheaf) (hF : IsAdequate B F) :
    List.TFAE
      [IsZero (B.zariskiRestrictModule.obj F),
        IsParasitic S B.toOver F.val,
        IsParasiticFor.{u, w} S B.toOver (isTauCovering.{u, w} B) F.val,
        ∀ U : S.Opens, Subsingleton (F.val.obj (op (B.opensToBig.obj U))),
        ∃ (I : Type u) (U : I → S.Opens), (∀ i, IsAffineOpen (U i)) ∧ (⨆ i, U i) = ⊤ ∧
          ∀ i, Subsingleton (F.val.obj (op (B.opensToBig.obj (U i))))]
```

## Tag 06ZN, a lemma

[Tag 06ZN](https://stacks.math.columbia.edu/tag/06ZN) in the Stacks Project.

**`Stacks.Adequate.BigSite.isSerreClass_parasiticAdequate`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean#L525). The attribute's comment: “the subcategory of parasitic adequate modules is a Serre subcategory”.

> **[Stacks, Tag 06ZN], the Serre subcategory.** The parasitic adequate `𝒪`-modules form a
> Serre subcategory `𝒞` of `Adeq(𝒪)`: it is the kernel of the exact functor
> `v : Adeq(𝒪) ⥤ QCoh(𝒪_S)` (`Stacks.Adequate.BigSite.parasiticAdequate_eq_kernel`, which is
> [Stacks, Tag 06ZM]), and the kernel of an exact functor is a Serre subcategory
> ([Stacks, Tag 02MQ]). `v` is exact by
> `Stacks.Adequate.BigSite.preservesFiniteLimits_restrictModuleQCoh` and
> `Stacks.Adequate.BigSite.preservesFiniteColimits_restrictModuleQCoh`. The abelian structure on
> `Adeq(𝒪)` is [Stacks, Tag 06VQ] (1), `Stacks.Adequate.abelian_adequate`.

```lean
public instance BigSite.isSerreClass_parasiticAdequate : B.parasiticAdequate.IsSerreClass
```

**`Stacks.Adequate.BigSite.isLocalization_restrictModuleQCoh`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/Parasitic.lean#L554). The attribute's comment: “the functor `v` induces an equivalence `Adeq(𝒪)/𝒞 = QCoh(𝒪_S)`: `v` is a localization functor for the isomorphisms modulo the Serre subcategory `𝒞`”.

> **[Stacks, Tag 06ZN], the quotient equivalence.** The functor `v : Adeq(𝒪) ⥤ QCoh(𝒪_S)`
> induces an equivalence `Adeq(𝒪)/𝒞 ≌ QCoh(𝒪_S)`, where `𝒞` is the Serre subcategory of
> parasitic adequate modules and `Adeq(𝒪)/𝒞` is the Serre quotient, the localization of `Adeq(𝒪)`
> at the morphisms which are isomorphisms modulo `𝒞` ([Stacks, Tag 02MS]): `v` is a localization
> functor for that class of morphisms.
>
> The proof is the source's. `v` is exact, its kernel is `𝒞`, so the morphisms inverted by `v`
> are those which are isomorphisms modulo `𝒞`; and `v` has the fully faithful left adjoint
> `u : QCoh(𝒪_S) ⥤ Adeq(𝒪)` of [Stacks, Tag 06VN] (`Stacks.Adequate.BigSite.adeqAdjunction`,
> the unit `𝓕 → vu𝓕` being an isomorphism), which makes the induced functor `v̄` essentially
> surjective and fully faithful (`CategoryTheory.Adjunction.isLocalization'`).

```lean
public instance BigSite.isLocalization_restrictModuleQCoh :
    B.restrictModuleQCoh.IsLocalization B.parasiticAdequate.isoModSerre
```

## Tag 06ZP, a lemma

[Tag 06ZP](https://stacks.math.columbia.edu/tag/06ZP) in the Stacks Project.

**`Stacks.Adequate.isAdequate_and_isParasitic_directImage_ofAmbient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDirectImage.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateModules/ParasiticDirectImage.lean#L367).

> **[Stacks, Tag 06ZP].** Let `f : T ⟶ S` be a quasi-compact and quasi-separated morphism of
> schemes and let `𝓕` be a parasitic adequate `𝒪_T`-module on `(Sch/T)_τ`, for `τ` any of the five
> topologies `Zar`, `étale`, `smooth`, `syntomic`, `fppf`. Then the pushforward `f_*𝓕` and every
> higher direct image `R^i f_*𝓕` are parasitic adequate `𝒪_S`-modules on `(Sch/S)_τ`.
>
> `(Sch/S)_τ` and `(Sch/T)_τ` are the localizations at `S` and at `T` of one ambient big `τ`-site
> `𝒮`, as they are in the source (`Stacks.Adequate.BigSite.ofAmbient`; by
> `Stacks.Adequate.BigSite.exists_eq_ofAmbient` every chosen big site is one). `f_*` is the direct
> image of [Stacks, Tag 06VR] along the base change `V ↦ V ×_S T`
> (`Stacks.Adequate.ambientBaseChange`) with its first projection, and `R^i f_*` is its `i`-th right
> derived functor; nothing is assumed about either, since
> `Stacks.Adequate.isContinuous_ambientBaseChange` and
> `Stacks.Adequate.isBaseChangeAlong_ambientBaseChange` supply what Tag 06VR needs. The proof is
> `Stacks.Adequate.isAdequate_and_isParasitic_directImage`.

```lean
public theorem isAdequate_and_isParasitic_directImage_ofAmbient
    (F : SheafOfModules.{u} (BigSite.ofAmbient 𝒮 T hT).structureSheaf)
    (hF : IsAdequate (BigSite.ofAmbient 𝒮 T hT) F)
    (hpar : IsParasitic T (BigSite.ofAmbient 𝒮 T hT).toOver F.val)
    (hqc : QuasiCompact f) (hqs : QuasiSeparated f) :
    (IsAdequate (BigSite.ofAmbient 𝒮 S hS)
        ((directImage.{u, u} (BigSite.ofAmbient 𝒮 S hS) (BigSite.ofAmbient 𝒮 T hT)
          (ambientBaseChange 𝒮 hS hT f) (ambientBaseChangeFst 𝒮 hS hT f)).obj F) ∧
      IsParasitic S (BigSite.ofAmbient 𝒮 S hS).toOver
        ((directImage.{u, u} (BigSite.ofAmbient 𝒮 S hS) (BigSite.ofAmbient 𝒮 T hT)
          (ambientBaseChange 𝒮 hS hT f) (ambientBaseChangeFst 𝒮 hS hT f)).obj F).val) ∧
      ∀ i : ℕ, IsAdequate (BigSite.ofAmbient 𝒮 S hS)
          ((higherDirectImage.{u, u} (BigSite.ofAmbient 𝒮 S hS) (BigSite.ofAmbient 𝒮 T hT)
            (ambientBaseChange 𝒮 hS hT f) (ambientBaseChangeFst 𝒮 hS hT f) i).obj F) ∧
        IsParasitic S (BigSite.ofAmbient 𝒮 S hS).toOver
          ((higherDirectImage.{u, u} (BigSite.ofAmbient 𝒮 S hS) (BigSite.ofAmbient 𝒮 T hT)
            (ambientBaseChange 𝒮 hS hT f) (ambientBaseChangeFst 𝒮 hS hT f) i).obj F).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.6, Tag 06ZK](https://stacks.math.columbia.edu/tag/06ZK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
