---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.SmallSite.crystalConnectionCris, Crystalline.GlobalCrystallineSituation.SmallSite.crystalConnectionCris_isIntegrableConnection
statement: formalized
proof: formalized
---

# 60.15 Connections

Section 60.15 of the Stacks Project, [Tag 07J5](https://stacks.math.columbia.edu/tag/07J5). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07J6, a lemma

[Tag 07J6](https://stacks.math.columbia.edu/tag/07J6) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalConnectionCris`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalConnectionCris.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalConnectionCris.lean#L347). The attribute's comment: “the canonical connection ∇ : F ⟶ F ⊗_{𝒪_{X/S}} Ω_{X/S} of a crystal F on Cris(X/S), a morphism of abelian sheaves: on every T it is p₁^* s - p₀^* s on the first-order thickening T' of 07J2, read through (F ⊗ Ω_{X/S})_T = F_T ⊗ Ω_{T/S,δ}”.

> **The canonical connection of a crystal, as a morphism of abelian sheaves
> `∇ : F ⟶ F ⊗_{𝒪_{X/S}} Ω_{X/S}` on `Cris(X/S)`.**  On the ambient scheme `T` of every object it
> is the connection `p₁^* s - p₀^* s`, read through `(F ⊗ Ω_{X/S})_T = F_T ⊗ Ω_{T/S,δ}`
> (`crystalConnectionCrisApp_restrict`).

```lean
def crystalConnectionCris : abelianSheaf F ⟶ tensorDifferentialFormsSheaf F 1
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.crystalConnectionCris_isIntegrableConnection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalIntegrableConnectionCris.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/CrystalIntegrableConnectionCris.lean#L153). The attribute's comment: “a crystal F on Cris(X/S) has a canonical integrable connection: ∇ = crystalConnectionCris : F ⟶ F ⊗ Ω_{X/S}, a morphism of abelian sheaves, satisfies the Leibniz rule, is p₁^* s - p₀^* s on every T, its extension F ⊗ Ω ⟶ F ⊗ Ω² obeys ∇(s ⊗ ω) = ∇(s) ∧ ω + s ⊗ d ω, and ∇ ∘ ∇ = 0”.

> **A crystal `F` in `𝒪_{X/S}`-modules on `Cris(X/S)` comes equipped with a canonical integrable
> connection.**  The connection is
> `∇ = crystalConnectionCris : F ⟶ F ⊗_{𝒪_{X/S}} Ω_{X/S}`, a morphism of abelian sheaves on
> `Cris(X/S)`, and
>
> 1. (**it is a connection**) `∇(f s) = f ∇(s) + s ⊗ d f` for every object `A` and all sections `f`
>    of `𝒪_{X/S}` and `s` of `F` over `A`;
> 2. (**it is the canonical one**) on the ambient scheme `T` of every object, `∇(s)` is
>    `p₁^* s - p₀^* s` on the first-order thickening `T'` of [Stacks, Tag 07J2], read in
>    `F_T ⊗ Ω_{T/S,δ} ⊂ F_{T'}`;
> 3. the exterior product by a one-form is `(x ⊗ η) ∧ ω = x ⊗ (η ∧ ω)` on local pure tensors, and
>    the extension `crystalExtensionCris : F ⊗ Ω_{X/S} ⟶ F ⊗ Ω²_{X/S}` is given by the rule
>    `∇(s ⊗ ω) = ∇(s) ∧ ω + s ⊗ d ω` of [Stacks, Tag 07I0] and [Stacks, Section 60.15, Tag 07J5];
> 4. (**it is integrable**) `∇ ∘ ∇ = 0 : F ⟶ F ⊗ Ω²_{X/S}`.

```lean
theorem crystalConnectionCris_isIntegrableConnection (hF : IsSheafCrystal F) :
    ((∀ (A : CrystallineThickening S) (f : crysFormRing S A) (s : F.val.obj (op A)),
        (show tensorFormsModSec F 1 A from
          (crystalConnectionCris hF).hom.app (op A) (ULift.up (f • s))) =
          f • (show tensorFormsModSec F 1 A from
            (crystalConnectionCris hF).hom.app (op A) (ULift.up s)) +
          (show tensorFormsModSec F 1 A from
            (CategoryTheory.toSheafify (smallTopology S) (tensorDifferentialFormsPresheaf F 1)).app
              (op A) (ULift.up (formsTmul F s (formsD A f))))) ∧
      ∀ (A : CrystallineThickening S) (s : (abelianSheaf F).obj.obj (op A)),
        (firstOrderTensorInclusion F A).val.app (op ⊤)
            ((tensorFormsAmbientIsoOne A).hom.app (op ⊤)
              ((tensorDifferentialFormsSheaf F 1).obj.map (A.restrictOpenHom ⊤).op
                ((crystalConnectionCris hF).hom.app (op A) s))).down =
          crystalConnectionRaw F A ⊤ (F.val.map (A.restrictOpenHom ⊤).op s.down)) ∧
    ((∀ (A : CrystallineThickening S) (ω : (crysDifferentialForms S 1).obj (op A))
          (x : F.val.obj (op A)) (η : (crysDifferentialForms S 1).obj (op A)),
        crystalWedgeCrisApp F A ω
            ((CategoryTheory.toSheafify (smallTopology S) (tensorDifferentialFormsPresheaf F 1)).app
              (op A) (ULift.up (formsTmul F x η))) =
          (CategoryTheory.toSheafify (smallTopology S) (tensorDifferentialFormsPresheaf F 2)).app
            (op A) (ULift.up (formsTmul F x (formsWedgeOne η ω)))) ∧
      (∀ (A : CrystallineThickening S) (s : F.val.obj (op A))
          (ω : (crysDifferentialForms S 1).obj (op A)),
        (crystalExtensionCris hF).hom.app (op A)
            ((CategoryTheory.toSheafify (smallTopology S) (tensorDifferentialFormsPresheaf F 1)).app
              (op A) (ULift.up (formsTmul F s ω))) =
          crystalWedgeCrisApp F A ω ((crystalConnectionCris hF).hom.app (op A) (ULift.up s)) +
            (show (tensorDifferentialFormsSheaf F 2).obj.obj (op A) from
              (CategoryTheory.toSheafify (smallTopology S)
                (tensorDifferentialFormsPresheaf F 2)).app
                  (op A) (ULift.up (formsTmul F s (formsDeRham A ω))))) ∧
      crystalConnectionCris hF ≫ crystalExtensionCris hF = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.15, Tag 07J5](https://stacks.math.columbia.edu/tag/07J5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
