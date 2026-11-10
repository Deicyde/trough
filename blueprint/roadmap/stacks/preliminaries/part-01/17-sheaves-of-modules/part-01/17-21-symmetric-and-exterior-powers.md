---
declaration: section
origin: cited
lean: SheafOfModules.ringedSpaceAlgebras, SheafOfModules.exteriorPower_isSheafification, SheafOfModules.symmetricPower_isSheafification, SheafOfModules.symmetricAlgebra_stalk, PresheafOfModules.extPowStalkEquivOfStalkIso, SheafOfModules.exteriorAlgebra_stalk, SheafOfModules.symmetricPower_stalk, SheafOfModules.tensorPower_stalk
statement: formalized
proof: formalized
---

# 17.21 Symmetric and exterior powers

Section 17.21 of the Stacks Project, [Tag 01CF](https://stacks.math.columbia.edu/tag/01CF). 7 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01CF, the section

[Tag 01CF](https://stacks.math.columbia.edu/tag/01CF) in the Stacks Project.

**`SheafOfModules.ringedSpaceAlgebras`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AlgebraBundleStalk.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AlgebraBundleStalk.lean#L424). The attribute's comment: “the construction of the three algebras themselves, for a sheaf of modules on a ringed space, which is the object the lemmas 01CG, 01CH, 01CJ, 01CK and 01CL of the section are statements about; the section has no finer tag for it”.

> **The tensor, exterior and symmetric algebras of a sheaf of modules on a ringed space**, as
> the package Section 17.21 attaches to `F`: the three graded algebras, their three universal
> properties, the identification of the homogeneous pieces of `T(F)` with the tensor powers of `F`,
> the degree-zero identifications, the vanishing in negative degrees, the direct-sum presentation
> and the two quotient maps `T(F) ⟶ ⋀(F)` and `T(F) ⟶ Sym(F)`. It is `SheafOfModules.algebras`,
> i.e. `sheafifiedAlgebras`, at the site of open subsets of `X`, so each of the three algebras is
> the degreewise sheafification of its sectionwise counterpart, which is the section's own
> construction.

```lean
noncomputable def ringedSpaceAlgebras (F : SheafOfModules.{w} (structureSheafRing X)) :
    TensorExteriorSymmetricAlgebras (Opens.grothendieckTopology X.carrier) F
```

## Tag 01CG, a lemma

[Tag 01CG](https://stacks.math.columbia.edu/tag/01CG) in the Stacks Project.

**`SheafOfModules.exteriorPower_isSheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerComparison.lean, line 568](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerComparison.lean#L568). The attribute's comment: “exterior_power_sheafification: the exterior assertion, that `⋀ⁿ M` is the sheafification of `X ↦ ⋀ⁿ(M(X))`, with the comparison pinned on wedges of degree-one local sections. The symmetric assertion is `SheafOfModules.symmetricPower_isSheafification`; the tag states those two and nothing else, so that pair is its covering set.”.

> For a sheaf of modules `M` on a site with a sheaf of
> commutative rings `O♯`, and an exterior algebra `A` of `M` in the sense of Section 17.21, the
> degree-`n` exterior power `A.piece n` of `M` is the sheafification of the presheaf
> `X ↦ ⋀ⁿ_{O♯(X)}(M(X))`.
>
> The presheaf is exhibited together with the sectionwise identification of its sections with
> `⋀ⁿ_{O♯(X)}(M(X))` and the comparison morphism to `A.piece n`; the two equation families fix the
> restriction maps and the comparison morphism on wedges of degree-one generators, and the last
> conjunct is the sheafification assertion.

```lean
theorem exteriorPower_isSheafification (n : ℕ) :
    ∃ P : PresheafOfModules.{w} (toRingCat J Osharp).obj,
      ∃ e : ∀ X : Cᵒᵖ, P.obj X ≃ₗ[(toRingCat J Osharp).obj.obj X]
          ⋀[(toRingCat J Osharp).obj.obj X]^n (M.val.obj X),
        ∃ cmp : P ⟶ (SheafOfModules.forget (toRingCat J Osharp)).obj (A.piece (n : ℤ)),
          (∀ (X Y : Cᵒᵖ) (f : X ⟶ Y) (s : Fin n → M.val.obj X)
              (x : ⋀[(toRingCat J Osharp).obj.obj X]^n (M.val.obj X))
              (y : ⋀[(toRingCat J Osharp).obj.obj Y]^n (M.val.obj Y)),
            ((x : ExteriorAlgebra ((toRingCat J Osharp).obj.obj X) (M.val.obj X)) =
                ExteriorAlgebra.ιMulti ((toRingCat J Osharp).obj.obj X) n s) →
            ((y : ExteriorAlgebra ((toRingCat J Osharp).obj.obj Y) (M.val.obj Y)) =
                ExteriorAlgebra.ιMulti ((toRingCat J Osharp).obj.obj Y) n
                  fun i => M.val.map f (s i)) →
            e Y (P.map f ((e X).symm x)) = y) ∧
          (∀ (X : Cᵒᵖ) (s : Fin n → M.val.obj X)
              (x : ⋀[(toRingCat J Osharp).obj.obj X]^n (M.val.obj X)),
            ((x : ExteriorAlgebra ((toRingCat J Osharp).obj.obj X) (M.val.obj X)) =
                ExteriorAlgebra.ιMulti ((toRingCat J Osharp).obj.obj X) n s) →
            Hom.app cmp X ((e X).symm x) =
              A.toPresheafGradedAlgebra.homogeneousProdLeft X n
                fun i => gen.val.app X (s i)) ∧
          IsIso ((sheafificationHomEquiv (𝟙 (toRingCat J Osharp).obj)).symm cmp)
```

**`SheafOfModules.symmetricPower_isSheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerComparison.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerComparison.lean#L411). The attribute's comment: “symmetric_power_sheafification”.

> **Tag 01CG.** For a sheaf of modules `M` on a site with a sheaf of commutative rings `O♯`, and
> a symmetric algebra `A` of `M` in the sense of Section 17.21, the degree-`n` symmetric power
> `A.piece n` of `M` is the sheafification of the presheaf `X ↦ Symⁿ_{O♯(X)}(M(X))`.
>
> The presheaf is exhibited together with the sectionwise identification of its sections with
> `Symⁿ_{O♯(X)}(M(X))` and the comparison morphism to `A.piece n`; the two equation families fix
> the restriction maps and the comparison morphism on products of degree-one generators, and the
> last conjunct is the sheafification assertion.
>
> The symmetric algebra is a hypothesis rather than a chosen term: Section 17.21 pins it only up to
> canonical isomorphism, and `SheafOfModules.sectionwiseSymmetricAlgebra` together with
> `SheafOfModules.isSymmetricAlgebra_sectionwiseSymmetricAlgebra` and
> `SheafOfModules.GradedAlgebra.IsSymmetricAlgebra.comp_iso` shows the hypothesis is satisfiable for
> every `M`.

```lean
theorem symmetricPower_isSheafification (n : ℕ) :
    ∃ P : PresheafOfModules.{w} (toRingCat J Osharp).obj,
      ∃ e : ∀ X : Cᵒᵖ, P.obj X ≃ₗ[(toRingCat J Osharp).obj.obj X]
          SymPow.symmetricPower n ((toRingCat J Osharp).obj.obj X) (M.val.obj X),
        ∃ cmp : P ⟶ (SheafOfModules.forget (toRingCat J Osharp)).obj (A.piece (n : ℤ)),
          (∀ (X Y : Cᵒᵖ) (f : X ⟶ Y) (s : Fin n → M.val.obj X)
              (x : SymPow.symmetricPower n ((toRingCat J Osharp).obj.obj X) (M.val.obj X))
              (y : SymPow.symmetricPower n ((toRingCat J Osharp).obj.obj Y) (M.val.obj Y)),
            ((x : SymmetricAlgebra ((toRingCat J Osharp).obj.obj X) (M.val.obj X)) =
                ∏ i : Fin n, SymmetricAlgebra.ι ((toRingCat J Osharp).obj.obj X)
                  (M.val.obj X) (s i)) →
            ((y : SymmetricAlgebra ((toRingCat J Osharp).obj.obj Y) (M.val.obj Y)) =
                ∏ i : Fin n, SymmetricAlgebra.ι ((toRingCat J Osharp).obj.obj Y)
                  (M.val.obj Y) (M.val.map f (s i))) →
            e Y (P.map f ((e X).symm x)) = y) ∧
          (∀ (X : Cᵒᵖ) (s : Fin n → M.val.obj X)
              (x : SymPow.symmetricPower n ((toRingCat J Osharp).obj.obj X) (M.val.obj X)),
            ((x : SymmetricAlgebra ((toRingCat J Osharp).obj.obj X) (M.val.obj X)) =
                ∏ i : Fin n, SymmetricAlgebra.ι ((toRingCat J Osharp).obj.obj X)
                  (M.val.obj X) (s i)) →
            Hom.app cmp X ((e X).symm x) =
              A.toPresheafGradedAlgebra.homogeneousProdLeft X n
                fun i => gen.val.app X (s i)) ∧
          IsIso ((sheafificationHomEquiv (𝟙 (toRingCat J Osharp).obj)).symm cmp)
```

## Tag 01CH, a lemma

[Tag 01CH](https://stacks.math.columbia.edu/tag/01CH) in the Stacks Project.

**`SheafOfModules.symmetricAlgebra_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AlgebraStalkUngraded.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/AlgebraStalkUngraded.lean#L536). The attribute's comment: “the ungraded symmetric assertion `Sym(M)ₓ ≅ Sym(Mₓ)`, with the isomorphism pinned down by its values on germs of products of local sections in every degree. The tensor assertions are `SheafOfModules.tensorPower_stalk` and `SheafOfModules.tensorAlgebra_stalk`; the ungraded exterior assertion `⋀(M)ₓ ≅ ⋀(Mₓ)` for a sheaf is `SheafOfModules.exteriorAlgebra_stalk` in `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorStalkUngraded`, and the degreewise exterior assertion is `PresheafOfModules.extPowStalkEquivOfStalkIso`. With those the three ungraded isomorphisms the source asserts are all proved”. References: EGA II (1.7.4), “(S(E))_s = S(E_s)”.

> **Tag 01CH, ungraded symmetric assertion.** For a sheaf of modules `M` on a topological space
> with a sheaf of commutative rings `O♯`, a symmetric algebra `A` of `M` in the sense of Section
> 17.21, and a point `x`, there is a canonical isomorphism of `O_x`-modules
>
> `Sym(M)_x ≅ Sym_{O_x}(M_x)`,
>
> where `Sym(M)` is the coproduct `∐ n, Symⁿ M` of the homogeneous pieces of `A`.
>
> It is canonical in the sense Tag 01CH means: its value is prescribed on the germ of every local
> section of the form `s₀ ⋯ sₙ₋₁`, in every degree `n`, namely the product of the germs of the
> `sᵢ`; such products span each symmetric power of the stalk
> (`SymmetricAlgebra.symmetricPower_eq_span_prod_ι`) and the symmetric powers span `Sym(M_x)`
> (`SymmetricAlgebra.directSumSymmetricPowerEquiv`), so no other linear map has that behaviour.
>
> The symmetric algebra is a hypothesis rather than a chosen term because Section 17.21 pins it
> only up to canonical isomorphism;
> `SheafOfModules.isSymmetricAlgebra_sectionwiseSymmetricAlgebra_val` shows the hypothesis is
> satisfiable for every `M`, and
> `SheafOfModules.TensorExteriorSymmetricAlgebras.symmetricAlgebraStalkEquiv` discharges it from a
> package of the three algebras of Section 17.21.
>
> The tag carries a clause comment: this declaration carries the ungraded symmetric assertion
> alone. The two tensor assertions are `SheafOfModules.tensorPower_stalk` and
> `SheafOfModules.tensorAlgebra_stalk` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.TensorPowerStalk`. The ungraded *exterior*
> assertion `⋀(M)ₓ ≅ ⋀(Mₓ)` for a sheaf is `SheafOfModules.exteriorAlgebra_stalk` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorStalkUngraded`, which is built from
> `SheafOfModules.natStalkCoprodEquiv` below exactly as this declaration is; the ungraded statement
> for a **presheaf** of modules, `(⋀ F)ₓ ≅ ⋀(Fₓ)`, is `PresheafOfModules.extAlgStalkRingEquiv` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorPowerStalk` and the degreewise sheaf
> statement is `PresheafOfModules.extPowStalkEquivOfStalkIso` there.

```lean
theorem symmetricAlgebra_stalk (x : ↥X) :
    ∃ cmp : ↑(TopCat.Presheaf.stalk (∐ fun n : ℕ => A.piece (n : ℤ)).val.presheaf x)
        ≃ₗ[↑(TopCat.Presheaf.stalk Osharp.obj x)]
        SymmetricAlgebra ↑(TopCat.Presheaf.stalk Osharp.obj x)
          ↑(TopCat.Presheaf.stalk M.val.presheaf x),
      ∀ (n : ℕ) (U : Opens ↥X) (hx : x ∈ U) (s : Fin n → M.val.obj (op U)),
        cmp (TopCat.Presheaf.germ (∐ fun m : ℕ => A.piece (m : ℤ)).val.presheaf U x hx
            ((Sigma.ι (fun m : ℕ => A.piece (m : ℤ)) n).val.app (op U)
              (A.toPresheafGradedAlgebra.homogeneousProd (op U) n
                fun i => gen.val.app (op U) (s i)))) =
          ∏ i : Fin n, SymmetricAlgebra.ι ↑(TopCat.Presheaf.stalk Osharp.obj x)
            ↑(TopCat.Presheaf.stalk M.val.presheaf x)
            (TopCat.Presheaf.germ M.val.presheaf U x hx (s i))
```

**`PresheafOfModules.extPowStalkEquivOfStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerStalk.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerStalk.lean#L792). The attribute's comment: “the exterior assertion in each graded degree `n`: `(⋀ⁿ M)ₓ ≅ ⋀ⁿ(Mₓ)`, with the isomorphism pinned by `extPowStalkEquivOfStalkIso_germ_ιMulti` as the map carrying the germ of a wedge of local sections to the wedge of their germs. The symmetric assertion is `PresheafOfModules.symPowStalkEquivOfStalkIso`. The graded-to-ungraded passage is not proved here; it is `SheafOfModules.exteriorAlgebra_stalk` in `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorStalkUngraded`, which is the ungraded `⋀(M)ₓ ≅ ⋀(Mₓ)` that the source actually asserts.”. References: EGA 0 (4.1.5), “more general”.

> **The stalk of a sheafification of the sectionwise exterior powers.** If `φ` exhibits `Q` as
> having the same stalks as the presheaf `U ↦ ⋀ⁿ_{R(U)}(F(U))` — which the sheafification unit
> does, by `PresheafOfModules.isIso_stalkFunctor_map_toSheafify` — then the stalk of `Q` at `x` is
> `⋀ⁿ_{R_x}(F_x)`.
>
> This is the form the exterior assertion of Stacks Tag 01CH is consumed in: the degree-`n`
> exterior power of a sheaf of modules on a ringed space *is* the sheafification of the sectionwise
> exterior powers, so taking `Q` to be that sheafification and `φ` its unit computes the stalk of
> `⋀ⁿ F`. The isomorphism is pinned by `extPowStalkEquivOfStalkIso_germ_ιMulti`, which is the
> reason this and not an abstract uniqueness isomorphism is what the tag asserts.

```lean
noncomputable def extPowStalkEquivOfStalkIso (n : ℕ)
    {Q : PresheafOfModules.{u} (R ⋙ forget₂ CommRingCat.{u} RingCat.{u})}
    (φ : extPow n F ⟶ Q)
    (h : IsIso ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u} x).map
      ((toPresheaf _).map φ))) :
    ↑(TopCat.Presheaf.stalk Q.presheaf x) ≃ₗ[↑(R.stalk x)]
      ⋀[↑(R.stalk x)]^n ↑(TopCat.Presheaf.stalk F.presheaf x)
```

**`SheafOfModules.exteriorAlgebra_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorStalkUngraded.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorStalkUngraded.lean#L346). The attribute's comment: “the ungraded exterior assertion `⋀(M)ₓ ≅ ⋀(Mₓ)` — one of the three isomorphisms the source asserts — with the isomorphism pinned down by its values on germs of wedges of local sections in every degree. The ungraded symmetric assertion `Sym(M)ₓ ≅ Sym(Mₓ)` is `SheafOfModules.symmetricAlgebra_stalk`. The ungraded tensor assertion `T(M)ₓ ≅ T(Mₓ)` is not covered here. The degreewise clauses, which are this library's convention and not assertions of the source, are `SheafOfModules.symmetricPower_stalk` and `PresheafOfModules.extPowStalkEquivOfStalkIso`.”.

> **Tag 01CH, ungraded exterior assertion.** For a sheaf of modules `M` on a topological space
> with a sheaf of commutative rings `O♯`, an exterior algebra `A` of `M` in the sense of Section
> 17.21, and a point `x`, there is a canonical isomorphism of `O_x`-modules
>
> `⋀(M)_x ≅ ⋀_{O_x}(M_x)`,
>
> where `⋀(M)` is the coproduct `∐ n, ⋀ⁿ M` of the homogeneous pieces of `A`.
>
> It is canonical in the sense Tag 01CH means: its value is prescribed on the germ of every local
> section of the form `s₀ ∧ ⋯ ∧ s_{n-1}`, in every degree `n`, namely the wedge of the germs of the
> `sᵢ`; such wedges span each exterior power of the stalk
> (`ExteriorAlgebra.ιMulti_span_fixedDegree`) and the exterior powers span `⋀(M_x)`
> (`ExteriorAlgebra.gradedAlgebra`), so no other linear map has that behaviour.
>
> The exterior algebra is a hypothesis rather than a chosen term because Section 17.21 pins it only
> up to canonical isomorphism; `SheafOfModules.isExteriorAlgebra_sectionwiseExteriorAlgebra_val`
> shows the hypothesis is satisfiable for every `M`, and
> `SheafOfModules.TensorExteriorSymmetricAlgebras.exteriorAlgebraStalkEquiv` discharges it from a
> package of the three algebras of Section 17.21.

```lean
theorem exteriorAlgebra_stalk (x : ↥X) :
    ∃ cmp : ↑(TopCat.Presheaf.stalk (∐ fun n : ℕ => A.piece (n : ℤ)).val.presheaf x)
        ≃ₗ[↑(TopCat.Presheaf.stalk Osharp.obj x)]
        ExteriorAlgebra ↑(TopCat.Presheaf.stalk Osharp.obj x)
          ↑(TopCat.Presheaf.stalk M.val.presheaf x),
      ∀ (n : ℕ) (U : Opens ↥X) (hx : x ∈ U) (s : Fin n → M.val.obj (op U)),
        cmp (TopCat.Presheaf.germ (∐ fun m : ℕ => A.piece (m : ℤ)).val.presheaf U x hx
            ((Sigma.ι (fun m : ℕ => A.piece (m : ℤ)) n).val.app (op U)
              (A.toPresheafGradedAlgebra.homogeneousProd (op U) n
                fun i => gen.val.app (op U) (s i)))) =
          ExteriorAlgebra.ιMulti ↑(TopCat.Presheaf.stalk Osharp.obj x) n
            fun i => TopCat.Presheaf.germ M.val.presheaf U x hx (s i)
```

**`SheafOfModules.symmetricPower_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricStalkSheaf.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricStalkSheaf.lean#L431). The attribute's comment: “the symmetric assertion in each graded degree `n`: `(Symⁿ M)ₓ ≅ Symⁿ(Mₓ)`, with the isomorphism pinned down by its values on germs of products of local sections. The ungraded `Sym(M)ₓ ≅ Sym(Mₓ)` is `SheafOfModules.symmetricAlgebra_stalk`; the exterior assertion in each degree is `PresheafOfModules.extPowStalkEquivOfStalkIso` and the ungraded `⋀(M)ₓ ≅ ⋀(Mₓ)` is `SheafOfModules.exteriorAlgebra_stalk`; the tensor assertions are `SheafOfModules.tensorPower_stalk` and `SheafOfModules.tensorAlgebra_stalk`. The three assertions the source makes are the ungraded ones; the degreewise statements, this one included, are this library's clause convention”. References: EGA II (1.7.4), “partial”.

> **Tag 01CH, symmetric clause, in graded degree `n`.** For a sheaf of modules `M` on a
> topological space with a sheaf of commutative rings `O♯`, a symmetric algebra `A` of `M` in the
> sense of Section 17.21, and a point `x`, there is a canonical isomorphism of `O_x`-modules
>
> `(Symⁿ M)_x ≅ Symⁿ_{O_x}(M_x)`.
>
> It is canonical in the sense Tag 01CH means: its value is prescribed on the germ of every local
> section of the form `s₀ ⋯ sₙ₋₁`, namely the product of the germs of the `sᵢ`, and such products
> span the target (`SymmetricAlgebra.symmetricPower_eq_span_prod_ι`), so no other linear map has
> that behaviour.
>
> The symmetric algebra is a hypothesis rather than a chosen term because Section 17.21 pins it only
> up to canonical isomorphism; `SheafOfModules.isSymmetricAlgebra_sectionwiseSymmetricAlgebra_val`
> shows the hypothesis is satisfiable for every `M`, and
> `SheafOfModules.TensorExteriorSymmetricAlgebras.symmetricPowerStalkEquiv` discharges it from a
> package of the three algebras of Section 17.21.
>
> The tag carries a clause comment: this declaration carries the symmetric degreewise assertion
> alone. The ungraded symmetric assertion `Sym(M)_x ≅ Sym(M_x)` is proved from this one in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.AlgebraStalkUngraded`, and the two tensor
> assertions are `SheafOfModules.tensorPower_stalk` and `SheafOfModules.tensorAlgebra_stalk` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.TensorPowerStalk`.
>
> The exterior assertion in each graded degree is
> `PresheafOfModules.extPowStalkEquivOfStalkIso` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorPowerStalk`, pinned on germs of wedges of
> local sections by `PresheafOfModules.extPowStalkEquivOfStalkIso_germ_ιMulti`. It is stated there
> for a presheaf of modules together with a morphism out of the sectionwise exterior powers which
> is a stalk isomorphism — the form a sheafification presentation supplies — rather than in the
> bundled framing used here; `SheafOfModules.exteriorPowerStalkEquiv` in
> `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorStalkUngraded` is the bundled form, and
> `SheafOfModules.exteriorAlgebra_stalk` there is the ungraded exterior assertion. See the
> implementation notes of this file.

```lean
theorem symmetricPower_stalk (n : ℕ) (x : ↥X) :
    ∃ cmp : ↑(TopCat.Presheaf.stalk (A.piece (n : ℤ)).val.presheaf x)
        ≃ₗ[↑(TopCat.Presheaf.stalk Osharp.obj x)]
        SymPow.symmetricPower n ↑(TopCat.Presheaf.stalk Osharp.obj x)
          ↑(TopCat.Presheaf.stalk M.val.presheaf x),
      ∀ (U : Opens ↥X) (hx : x ∈ U) (s : Fin n → M.val.obj (op U)),
        (cmp (TopCat.Presheaf.germ (A.piece (n : ℤ)).val.presheaf U x hx
              (A.toPresheafGradedAlgebra.homogeneousProd (op U) n
                fun i => gen.val.app (op U) (s i))) :
            SymmetricAlgebra ↑(TopCat.Presheaf.stalk Osharp.obj x)
              ↑(TopCat.Presheaf.stalk M.val.presheaf x)) =
          ∏ i : Fin n, SymmetricAlgebra.ι ↑(TopCat.Presheaf.stalk Osharp.obj x)
            ↑(TopCat.Presheaf.stalk M.val.presheaf x)
            (TopCat.Presheaf.germ M.val.presheaf U x hx (s i))
```

**`SheafOfModules.tensorPower_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerStalk.lean, line 986](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerStalk.lean#L986). The attribute's comment: “the tensor assertion in each graded degree `n`: `(Tⁿ M)ₓ ≅ Tⁿ(Mₓ)` for a sheaf of modules, with the isomorphism pinned down by its values on germs of ordered tensors of local sections. The ungraded `T(M)ₓ ≅ T(Mₓ)` is `SheafOfModules.tensorAlgebra_stalk`; the symmetric assertions are `SheafOfModules.symmetricPower_stalk` and `SheafOfModules.symmetricAlgebra_stalk`; the exterior assertion is not carried here”.

> For a sheaf of modules `M` on a topological space with a sheaf of commutative rings `O♯`, a
> tensor algebra `A` of `M` in the sense of Section 17.21, and a point `x`, there is an isomorphism
> of `O_x`-modules
>
> `(Tⁿ M)ₓ ≅ Tⁿ_{O_x}(M_x)`
>
> sending the germ of every local section coming from an ordered tensor `s₀ ⊗ ⋯ ⊗ s_{n-1}` to the
> ordered tensor of the germs of the `sᵢ`.

```lean
theorem tensorPower_stalk (n : ℕ) (x : ↥X) :
    ∃ cmp : ↑(TopCat.Presheaf.stalk (A.piece (n : ℤ)).val.presheaf x)
        ≃ₗ[↑(TopCat.Presheaf.stalk Osharp.obj x)]
        TensorAlgebra.gradedPiece ↑(TopCat.Presheaf.stalk Osharp.obj x) n
          ↑(TopCat.Presheaf.stalk M.val.presheaf x),
      ∀ (U : Opens ↥X) (hx : x ∈ U) (s : Fin n → M.val.obj (op U)),
        cmp (TopCat.Presheaf.germ (A.piece (n : ℤ)).val.presheaf U x hx
              (PresheafOfModules.Hom.app (tensorAlgPieceIso A gen hA (n : ℤ)).hom.val (op U)
                (PresheafOfModules.Hom.app (PresheafOfModules.sheafifyUnit
                    (toRingCatMap (Opens.grothendieckTopology ↥X) (𝟙 Osharp.obj))
                    (PresheafOfModules.tensorPow n M.val)) (op U)
                  (TensorAlgebra.ιMultiPow
                    ((Osharp.obj ⋙ forget₂ CommRingCat.{u} RingCat.{u}).obj (op U)) n s)))) =
          TensorAlgebra.ιMultiPow ↑(TopCat.Presheaf.stalk Osharp.obj x) n
            fun i => TopCat.Presheaf.germ M.val.presheaf U x hx (s i)
```

**`SheafOfModules.tensorAlgebra_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerStalk.lean, line 1065](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerStalk.lean#L1065). The attribute's comment: “the ungraded tensor assertion `T(M)ₓ ≅ T(Mₓ)`, with the isomorphism pinned down by its values on germs of ordered tensors of local sections in every degree. The degreewise `(Tⁿ M)ₓ ≅ Tⁿ(Mₓ)` is `SheafOfModules.tensorPower_stalk`; the symmetric assertions are `SheafOfModules.symmetricPower_stalk` and `SheafOfModules.symmetricAlgebra_stalk`; the exterior assertion is not carried here”.

> For a sheaf of modules `M` on a topological space with a sheaf of commutative rings `O♯`, a
> tensor algebra `A` of `M` in the sense of Section 17.21, and a point `x`, there is an isomorphism
> of `O_x`-modules
>
> `T(M)ₓ ≅ T_{O_x}(M_x)`,
>
> where `T(M)` is the coproduct `∐ n, Tⁿ M` of the homogeneous pieces of `A`, sending the germ of
> every local section coming from an ordered tensor `s₀ ⊗ ⋯ ⊗ s_{n-1}`, in every degree `n`, to the
> ordered tensor of the germs of the `sᵢ`.

```lean
theorem tensorAlgebra_stalk (x : ↥X) :
    ∃ cmp : ↑(TopCat.Presheaf.stalk (∐ fun n : ℕ => A.piece (n : ℤ)).val.presheaf x)
        ≃ₗ[↑(TopCat.Presheaf.stalk Osharp.obj x)]
        TensorAlgebra ↑(TopCat.Presheaf.stalk Osharp.obj x)
          ↑(TopCat.Presheaf.stalk M.val.presheaf x),
      ∀ (n : ℕ) (U : Opens ↥X) (hx : x ∈ U) (s : Fin n → M.val.obj (op U)),
        cmp (TopCat.Presheaf.germ (∐ fun m : ℕ => A.piece (m : ℤ)).val.presheaf U x hx
            ((Sigma.ι (fun m : ℕ => A.piece (m : ℤ)) n).val.app (op U)
              (PresheafOfModules.Hom.app (tensorAlgPieceIso A gen hA (n : ℤ)).hom.val (op U)
                (PresheafOfModules.Hom.app (PresheafOfModules.sheafifyUnit
                    (toRingCatMap (Opens.grothendieckTopology ↥X) (𝟙 Osharp.obj))
                    (PresheafOfModules.tensorPow n M.val)) (op U)
                  (TensorAlgebra.ιMultiPow
                    ((Osharp.obj ⋙ forget₂ CommRingCat.{u} RingCat.{u}).obj (op U)) n s))))) =
          TensorAlgebra.ιMulti ↑(TopCat.Presheaf.stalk Osharp.obj x) n
            fun i => TopCat.Presheaf.germ M.val.presheaf U x hx (s i)
```

## Tag 01CI, a lemma

[Tag 01CI](https://stacks.math.columbia.edu/tag/01CI) in the Stacks Project.

**`Stacks.PullbackExteriorAlgebra.exteriorAlgebraPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraPullbackIso.lean, line 877](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraPullbackIso.lean#L877). The attribute's comment: “pullback_exterior_algebra: the EXTERIOR algebra clause only; symmetric NOT proved”.

> **Stacks 01CI for the exterior algebra of a sheaf of modules.** For a morphism of ringed
> spaces `f : X ⟶ Y` and a sheaf of `𝒪_Y`-modules `M`, the pullback of the exterior algebra of `M`
> is canonically isomorphic to the exterior algebra of `f^*M`, degreewise and on the underlying
> direct-sum sheaf, compatibly with the products, the units and the degree-one generators.
>
> This covers the **exterior algebra** clause of Tag 01CI only. The tensor-algebra clause is
> `Stacks.PullbackAlgebra.pullbackTensorPieceIso` and `pullbackTensorSheafIso`; the
> symmetric-algebra clause is **not** proved here. Both exterior algebras are given by their
> universal properties (`SheafOfModules.GradedAlgebra.IsExteriorAlgebra`) rather than by a
> construction, so nothing here depends on an unconstructed exterior algebra.

```lean
noncomputable def exteriorAlgebraPullbackIso (hA : IsExteriorAlgebra A ι)
    (hB : IsExteriorAlgebra B κ) : ExteriorAlgebraPullbackIso f A ι B κ
```

**`Stacks.PullbackExteriorAlgebra.exteriorAlgebraPullbackIso_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraPullbackIso.lean, line 892](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorAlgebraPullbackIso.lean#L892). The attribute's comment: “pullback_exterior_algebra: canonicality of the EXTERIOR algebra comparison only”.

> **The comparison of Stacks 01CI is unique.** Compatibility with multiplication, with the
> unit and with the degree-one generators on the pullback-unit sections determines the comparison
> in every degree, and the restriction to the homogeneous summands then determines the comparison
> of the underlying direct-sum sheaves.

```lean
theorem exteriorAlgebraPullbackIso_unique (hA : IsExteriorAlgebra A ι)
    (hB : IsExteriorAlgebra B κ) (e : ExteriorAlgebraPullbackIso f A ι B κ) :
    e = exteriorAlgebraPullbackIso f A ι B κ hA hB
```

**`Stacks.PullbackAlgebra.pullbackTensorPieceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackAlgebraIso.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackAlgebraIso.lean#L331). The attribute's comment: “the tensor algebra only. The exterior and symmetric algebras are NOT proved here; see the implementation notes for the two missing inputs.”.

> The pullback of the degree-`n` piece of the tensor algebra of `F` is the degree-`n` piece of
> the tensor algebra of `f^*F`.

```lean
noncomputable def pullbackTensorPieceIso (n : ℕ) :
    (pullbackFunctor f).obj (S.tensor.piece (n : ℤ)) ≅ T.tensor.piece (n : ℤ)
```

**`Stacks.PullbackAlgebra.pullbackTensorSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackAlgebraIso.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackAlgebraIso.lean#L393). The attribute's comment: “the tensor algebra only, on the underlying direct-sum sheaf. The exterior and symmetric algebras are NOT proved here.”.

> The pullback of the underlying direct-sum sheaf of the tensor algebra of `F` is the
> underlying direct-sum sheaf of the tensor algebra of `f^*F`.

```lean
noncomputable def pullbackTensorSheafIso :
    (pullbackFunctor f).obj S.tensorAlgebraSheaf ≅ T.tensorAlgebraSheaf
```

**`Stacks.RingedSpace.pullbackSymmetricPieceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SymmetricPullback/Iso.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SymmetricPullback/Iso.lean#L94). The attribute's comment: “symmetric algebra”. References: EGA II (1.7.5), “partial”.

> **Stacks 01CI for the symmetric algebra.** For a morphism of ringed spaces `f : X ⟶ Y` and
> a sheaf of `𝒪_Y`-modules `F`, the pullback of the degree-`n` symmetric power of `F` is the
> degree-`n` symmetric power of `f^*F`:
>
> `f^*(Symⁿ F) ≅ Symⁿ(f^*F)`.
>
> The two symmetric algebras are given by their universal property, so this is a statement about
> *the* symmetric algebras and not about one construction of them.

```lean
noncomputable def pullbackSymmetricPieceIso (hA : IsSymmetricAlgebra A ι)
    (hB : IsSymmetricAlgebra B κ) (n : ℤ) :
    (pullbackFunctor f).obj (A.piece n) ≅ B.piece n
```

**`Stacks.RingedSpace.pullbackSymmetricPieceIsoOfRingedSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SymmetricPullback/Iso.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SymmetricPullback/Iso.lean#L137). The attribute's comment: “symmetric algebra, at the constructed symmetric algebras”. References: EGA II (1.7.5), “partial”.

> **Stacks 01CI for the symmetric algebra, at the constructed symmetric algebras.** For a
> morphism of ringed spaces `f : X ⟶ Y` and a sheaf of `𝒪_Y`-modules `F`, the pullback of the
> degree-`n` symmetric power of `F` is the degree-`n` symmetric power of `f^*F`, both taken in
> `SheafOfModules.ringedSpaceAlgebras`.

```lean
noncomputable def pullbackSymmetricPieceIsoOfRingedSpace
    (G : SheafOfModules.{u} (structureRingSheaf Y)) (n : ℤ) :
    (pullbackFunctor f).obj ((SheafOfModules.ringedSpaceAlgebras Y G).symmetric.piece n) ≅
      (SheafOfModules.ringedSpaceAlgebras X
        ((pullbackFunctor f).obj G)).symmetric.piece n
```

## Tag 01CJ, a lemma

[Tag 01CJ](https://stacks.math.columbia.edu/tag/01CJ) in the Stacks Project.

**`SheafOfModules.ExtPresentation.epi_extDesc_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPresentationExact.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPresentationExact.lean#L334). The attribute's comment: “exterior case, surjectivity clause: the second map of the sequence is an epimorphism, in every degree and with no exactness hypothesis. Exactness at the middle term is covered, by `SheafOfModules.ExtPresentation.exteriorPresentation_exact` below, which carries that clause and states the sequence of the source. The symmetric counterparts are `SheafOfModules.SymPresentation.epi_symDesc_app` and `SheafOfModules.SymPresentation.symmetricPresentation_exact`.”.

> **The surjectivity clause of Stacks Tag 01CJ for exterior powers.** If `p : M₁ ⟶ M` is an
> epimorphism of sheaves of modules on a space, `A'` is an exterior algebra of `M₁` and `B'` an
> exterior algebra of `M`, then the induced map `⋀ⁿ(M₁) ⟶ ⋀ⁿ(M)` is an epimorphism in every degree.
> This is the clause `⟶ 0` of the sequence Tag 01CJ asserts.
>
> The hypothesis `n ≥ 1` of the source is not needed: the statement holds in degree `0` too, where
> both powers are the structure sheaf.

```lean
theorem epi_extDesc_app [Epi p] (n : ℕ) : Epi ((extDesc ι κ hA' hB' p).app (n : ℤ))
```

**`SheafOfModules.ExtPresentation.exteriorPresentation_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPresentationExact.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPresentationExact.lean#L600). The attribute's comment: “exterior case, in full: the sequence `M₂ ⊗ ⋀^k(M₁) ⟶ ⋀^{k+1}(M₁) ⟶ ⋀^{k+1}(M) ⟶ 0` is exact at the middle term and its second map is an epimorphism. The surjectivity clause alone, in every degree and with no exactness hypothesis, is `SheafOfModules.ExtPresentation.epi_extDesc_app`. With the symmetric pair `SheafOfModules.SymPresentation.epi_symDesc_app` and `SheafOfModules.SymPresentation.symmetricPresentation_exact` this completes the tag: the source states the two clauses for the symmetric and the exterior powers and nothing else.”.

> **Stacks Tag 01CJ for exterior powers.** Let `M₂ --q--> M₁ --p--> M ⟶ 0` be a presentation of
> a sheaf of modules on a topological space with a sheaf of commutative rings — `p` an epimorphism
> and the complex exact at `M₁` — let `A'` be an exterior algebra of `M₁` and `B'` one of `M`. Then
> for every `k` the three-term sequence
>
> `M₂ ⊗ ⋀^k(M₁) ⟶ ⋀^{k+1}(M₁) ⟶ ⋀^{k+1}(M) ⟶ 0`
>
> is exact at the middle term and its second map is an epimorphism, which is the exactness the
> source asserts in every degree `n = k + 1 ≥ 1`.

```lean
theorem exteriorPresentation_exact (hS : (ShortComplex.mk q p hqp).Exact) [Epi p] (k : ℕ) :
    (extComplex ι κ hA' hB' p q hqp k).Exact ∧
      Epi (extComplex ι κ hA' hB' p q hqp k).g
```

**`SheafOfModules.SymPresentation.epi_symDesc_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerPresentation.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerPresentation.lean#L380). The attribute's comment: “symmetric case, surjectivity clause: the second map of the sequence is an epimorphism, in every degree and with no exactness hypothesis. Exactness at the middle term is covered, by `SheafOfModules.SymPresentation.symmetricPresentation_exact` in `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.SymmetricPresentationExact`, which carries that clause and states the sequence of the source. The exterior case is covered too, by `SheafOfModules.ExtPresentation.epi_extDesc_app` and `SheafOfModules.ExtPresentation.exteriorPresentation_exact` in `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorPresentationExact`; those four declarations are the tag's covering set.”.

> **The surjectivity clause of Stacks Tag 01CJ for symmetric powers.** If `p : M₁ ⟶ M` is an
> epimorphism of sheaves of modules on a space, `A'` is a symmetric algebra of `M₁` and `B'` a
> symmetric algebra of `M`, then the induced map `Symⁿ(M₁) ⟶ Symⁿ(M)` is an epimorphism in every
> degree. This is the clause `⟶ 0` of the sequence Tag 01CJ asserts.
>
> The hypothesis `n ≥ 1` of the source is not needed: the statement holds in degree `0` too, where
> both powers are the structure sheaf.

```lean
theorem epi_symDesc_app [Epi p] (n : ℕ) : Epi ((symDesc ι κ hA' hB' p).app (n : ℤ))
```

**`SheafOfModules.SymPresentation.symmetricPresentation_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPresentationExact.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPresentationExact.lean#L528). The attribute's comment: “symmetric case, in full: the sequence `M₂ ⊗ Sym^k(M₁) ⟶ Sym^{k+1}(M₁) ⟶ Sym^{k+1}(M) ⟶ 0` is exact at the middle term and its second map is an epimorphism. The surjectivity clause alone, in every degree and with no exactness hypothesis, is `SheafOfModules.SymPresentation.epi_symDesc_app`. The exterior case is covered too, by `SheafOfModules.ExtPresentation.epi_extDesc_app` and `SheafOfModules.ExtPresentation.exteriorPresentation_exact` in `StacksFrontier.Algebra.Category.ModuleCat.Sheaf.ExteriorPresentationExact`; those four declarations are the tag's covering set”. References: EGA 0 (19.5.1), “more general”.

> **Stacks Tag 01CJ for symmetric powers.** Let `M₂ --q--> M₁ --p--> M ⟶ 0` be a presentation of
> a sheaf of modules on a topological space with a sheaf of commutative rings — `p` an epimorphism
> and the complex exact at `M₁` — let `A'` be a symmetric algebra of `M₁` and `B'` one of `M`. Then
> for every `k` the three-term sequence
>
> `M₂ ⊗ Sym^k(M₁) ⟶ Sym^{k+1}(M₁) ⟶ Sym^{k+1}(M) ⟶ 0`
>
> is exact at the middle term and its second map is an epimorphism, which is the exactness the
> source asserts in every degree `n = k + 1 ≥ 1`.
>
> The tag carries a clause comment: the surjectivity clause is also carried, at greater generality,
> by `SheafOfModules.SymPresentation.epi_symDesc_app`, and the exterior half of Tag 01CJ is not
> proved anywhere. See this file's implementation notes.

```lean
theorem symmetricPresentation_exact (hS : (ShortComplex.mk q p hqp).Exact) [Epi p] (k : ℕ) :
    (symComplex ι κ hA' hB' q p hqp k).Exact ∧ Epi (symComplex ι κ hA' hB' q p hqp k).g
```

**`SheafOfModules.exact_and_epi_symmetricPresentationShortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SymmetricSituation/PowerExact.lean, line 791](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SymmetricSituation/PowerExact.lean#L791). The attribute's comment: “symmetric powers”.

> **Stacks Tag 01CJ, symmetric powers.** Let `M₂ --q--> M₁ --p--> M --> 0` be an exact
> sequence of sheaves of modules on a ringed site, and let `n = 1 + k` with `k ≥ 0`. Then
>
> `M₂ ⊗ Sym^k(M₁) ⟶ Symⁿ(M₁) ⟶ Symⁿ(M) ⟶ 0`
>
> is exact: the complex is exact at the middle term and its second map is an epimorphism.

```lean
theorem exact_and_epi_symmetricPresentationShortComplex (q : M₂ ⟶ M₁) (p : M₁ ⟶ M)
    (hqp : q ≫ p = 0) [Epi p] (hex : (ShortComplex.mk q p hqp).Exact)
    (k n : ℤ) (hk : 0 ≤ k) (hn : 1 + k = n) :
    (GradedAlgebra.symmetricPresentationShortComplex
        (isSymmetricAlgebra_sheafifiedSymmetricAlgebra J M₁)
        (isSymmetricAlgebra_sheafifiedSymmetricAlgebra J M).isUniversal.1
        q p hqp k n hn).Exact ∧
      Epi (GradedAlgebra.symmetricPresentationShortComplex
        (isSymmetricAlgebra_sheafifiedSymmetricAlgebra J M₁)
        (isSymmetricAlgebra_sheafifiedSymmetricAlgebra J M).isUniversal.1
        q p hqp k n hn).g
```

## Tag 01CK, a lemma

[Tag 01CK](https://stacks.math.columbia.edu/tag/01CK) in the Stacks Project.

**`Stacks.SheafOfModules.isCoherent_exteriorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerCoherent.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerCoherent.lean#L297). The attribute's comment: “exterior powers of a coherent module, in positive degree”.

> **Each exterior power of positive degree of a coherent sheaf of modules on a ringed space is
> coherent.** This is clause (4) of [Stacks, Tag 01CK] for the exterior powers. The kernel `K` of
> the quotient map `Tⁿ(F) ⟶ ⋀ⁿ(F)` is of finite type over each member of a cover presenting `F`
> finitely, by Tag 01BP; hence coherent by Tag 01BY (1), since it is a subsheaf of the coherent
> sheaf `Tⁿ(F)`; hence `⋀ⁿ(F)` is coherent by Tag 01BY (3).

```lean
theorem isCoherent_exteriorPower [_root_.SheafOfModules.IsCoherent F]
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier) F) (n : ℕ) (hn : 0 < n) :
    _root_.SheafOfModules.IsCoherent (A.exteriorPower n)
```

**`Stacks.SheafOfModules.isFinitePresentation_exteriorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerFiniteType.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ExteriorPowerFiniteType.lean#L311). The attribute's comment: “exterior powers of a module of finite presentation”.

> **Each exterior power of a sheaf of modules of finite presentation on a ringed space is of
> finite presentation.** The covering family is the one that presents `F` finitely; no degree needs
> a smaller open, because
> `Stacks.SheafOfModules.exists_isFinite_presentation_exteriorPower_over` presents every degree
> finitely over that same open. This is clause (3) of [Stacks, Tag 01CK] for the exterior
> powers.

```lean
theorem isFinitePresentation_exteriorPower [F.IsFinitePresentation] (n : ℕ) :
    (A.exteriorPower n).IsFinitePresentation
```

**`Stacks.SheafOfModules.isLocallyFree_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePowers.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePowers.lean#L179). The attribute's comment: “symmetric powers of a locally free module”.

> **Each symmetric power of a locally free sheaf of modules is locally free.** This is clause
> (6) of [Stacks, Tag 01CK] for the symmetric powers: a covering trivialising `F` with index types
> `γ i` trivialises `Symⁿ F` with index types the degree-`n` multidegrees in `γ i`.

```lean
theorem isLocallyFree_symmetricPower
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras J F) (n : ℕ)
    [hF : F.IsLocallyFree] : (A.symmetricPower n).IsLocallyFree
```

**`Stacks.SheafOfModules.isLocallyFree_exteriorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePowers.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePowers.lean#L190). The attribute's comment: “exterior powers of a locally free module”. References: SGA 6 X (6.1), “special case”.

> **Each exterior power of a locally free sheaf of modules is locally free.** This is clause
> (6) of [Stacks, Tag 01CK] for the exterior powers: a covering trivialising `F` with index types
> `γ i` trivialises `⋀ⁿ F` with index types the `n`-element subsets of `γ i`.

```lean
theorem isLocallyFree_exteriorPower
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras J F) (n : ℕ)
    [hF : F.IsLocallyFree] : (A.exteriorPower n).IsLocallyFree
```

**`Stacks.SheafOfModules.isLocallyFree_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePowers.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreePowers.lean#L268). The attribute's comment: “tensor powers of a locally free module”.

> **Each tensor power of a locally free sheaf of modules is locally free.** This is clause (6)
> of [Stacks, Tag 01CK] for the tensor powers: a covering trivialising `F` with index types `γ i`
> trivialises `Tⁿ F` with index types the `n`-fold products of the `γ i`.

```lean
theorem isLocallyFree_tensorPower
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras J F) (n : ℕ)
    [hF : F.IsLocallyFree] : (A.tensor.piece (n : ℤ)).IsLocallyFree
```

**`Stacks.SheafOfModules.nonempty_localGeneratorsData_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean#L329). The attribute's comment: “symmetric powers of a module locally generated by sections”.

> **Each symmetric power of a sheaf of modules locally generated by sections on a ringed space
> is locally generated by sections.** This is clause (1) of [Stacks, Tag 01CK] for the symmetric
> powers.

```lean
theorem nonempty_localGeneratorsData_symmetricPower
    (hF : Nonempty (F.LocalGeneratorsData.{u, u, u, u})) (n : ℕ) :
    Nonempty ((A.symmetricPower n).LocalGeneratorsData.{u, u, u, u})
```

**`Stacks.SheafOfModules.nonempty_localGeneratorsData_exteriorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean#L338). The attribute's comment: “exterior powers of a module locally generated by sections”.

> **Each exterior power of a sheaf of modules locally generated by sections on a ringed space is
> locally generated by sections.** This is clause (1) of [Stacks, Tag 01CK] for the exterior
> powers.

```lean
theorem nonempty_localGeneratorsData_exteriorPower
    (hF : Nonempty (F.LocalGeneratorsData.{u, u, u, u})) (n : ℕ) :
    Nonempty ((A.exteriorPower n).LocalGeneratorsData.{u, u, u, u})
```

**`Stacks.SheafOfModules.isFiniteType_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean#L348). The attribute's comment: “symmetric powers of a module of finite type”. References: EGA II (1.7.7), “more general”.

> **Each symmetric power of a sheaf of modules of finite type on a ringed space is of finite
> type.** This is clause (2) of [Stacks, Tag 01CK] for the symmetric powers: the covering is the one
> on which `F` is generated by finitely many sections, and the index type produced in degree `n` is
> the set of degree-`n` multidegrees in the given one, hence finite.

```lean
theorem isFiniteType_symmetricPower
    [hF : _root_.SheafOfModules.IsFiniteType.{u, u, u} F] (n : ℕ) :
    _root_.SheafOfModules.IsFiniteType.{u, u, u} (A.symmetricPower n)
```

**`Stacks.SheafOfModules.isFiniteType_exteriorPower'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PowerLocalGenerators.lean#L361). The attribute's comment: “exterior powers of a module of finite type”.

> **Each exterior power of a sheaf of modules of finite type on a ringed space is of finite
> type.** This is clause (2) of [Stacks, Tag 01CK] for the exterior powers. The primed name
> distinguishes it from `Stacks.SheafOfModules.isFiniteType_exteriorPower`, which assumes `F` of
> finite presentation and is therefore not this clause.

```lean
theorem isFiniteType_exteriorPower'
    [hF : _root_.SheafOfModules.IsFiniteType.{u, u, u} F] (n : ℕ) :
    _root_.SheafOfModules.IsFiniteType.{u, u, u} (A.exteriorPower n)
```

**`Stacks.SheafOfModules.isQuasicoherent_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean#L763). The attribute's comment: “symmetric powers of a quasi-coherent module”.

> **Each symmetric power of a quasi-coherent sheaf of modules on a ringed space is
> quasi-coherent.** A presentation of the module over an open presents every symmetric power of it
> over that same open, by `Stacks.SheafOfModules.nonempty_presentation_symmetricPower_over`, so the
> covering family which presents the module presents the symmetric power too.

```lean
theorem isQuasicoherent_symmetricPower (n : ℕ) : (A.symmetricPower n).IsQuasicoherent
```

**`Stacks.SheafOfModules.isCoherent_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerCoherent.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerCoherent.lean#L304). The attribute's comment: “symmetric powers of a coherent module, in positive degree”.

> **Each symmetric power of positive degree of a coherent sheaf of modules on a ringed space is
> coherent.** This is clause (4) of [Stacks, Tag 01CK] for the symmetric powers. The sequence used
> is `⊕_{p < n - 1} Tⁿ(F) ⟶ Tⁿ(F) ⟶ Symⁿ(F) ⟶ 0`, whose first term is coherent by
> `Stacks.SheafOfModules.isCoherent_tensorPower` and `isCoherent_sigma`, so that closure of
> coherence under cokernels finishes.

```lean
theorem isCoherent_symmetricPower [_root_.SheafOfModules.IsCoherent F]
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier) F) (n : ℕ) (hn : 0 < n) :
    _root_.SheafOfModules.IsCoherent (A.symmetricPower n)
```

**`Stacks.SheafOfModules.isFinitePresentation_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerFiniteType.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SymmetricPowerFiniteType.lean#L169). The attribute's comment: “symmetric powers of a module of finite presentation”. References: EGA II (1.7.7), “special case”.

> **Each symmetric power of a sheaf of modules of finite presentation on a ringed space is of
> finite presentation.** This is clause (3) of [Stacks, Tag 01CK] for the symmetric powers. The
> covering family is the one that presents `F` finitely; no degree needs a smaller open, because
> `Stacks.SheafOfModules.exists_isFinite_presentation_symmetricPower_over` presents every degree
> finitely over that same open.

```lean
theorem isFinitePresentation_symmetricPower [F.IsFinitePresentation] (n : ℕ) :
    (A.symmetricPower n).IsFinitePresentation
```

**`Stacks.SheafOfModules.isCoherent_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCoherent.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerCoherent.lean#L98). The attribute's comment: “tensor powers of a coherent module, in positive degree”.

> **Each tensor power of positive degree of a coherent sheaf of modules on a ringed space is
> coherent.** This is clause (4) of [Stacks, Tag 01CK] for the tensor powers.

```lean
theorem isCoherent_tensorPower [_root_.SheafOfModules.IsCoherent F]
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier) F) (n : ℕ) (hn : 0 < n) :
    _root_.SheafOfModules.IsCoherent (A.tensor.piece (n : ℤ))
```

**`Stacks.SheafOfModules.isFinitePresentation_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerFiniteType.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerFiniteType.lean#L198). The attribute's comment: “tensor powers of a module of finite presentation”.

> **Each tensor power of a sheaf of modules of finite presentation on a ringed space is of
> finite presentation.** This is clause (3) of [Stacks, Tag 01CK] for the tensor powers. The
> covering family is the one that presents `F` finitely; no degree needs a smaller open, because
> `Stacks.SheafOfModules.exists_isFinite_presentation_tensorPiece_over` presents every degree
> finitely over that same open.

```lean
theorem isFinitePresentation_tensorPower [F.IsFinitePresentation] (n : ℕ) :
    (A.tensor.piece (n : ℤ)).IsFinitePresentation
```

**`Stacks.SheafOfModules.nonempty_localGeneratorsData_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerLocalGenerators.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerLocalGenerators.lean#L165). The attribute's comment: “tensor powers of a module locally generated by sections”.

> Each tensor power of a sheaf of modules locally generated by sections on a ringed space is
> locally generated by sections, on the same covering.

```lean
theorem nonempty_localGeneratorsData_tensorPower
    (hF : Nonempty (F.LocalGeneratorsData.{t, t, t, t})) (n : ℕ) :
    Nonempty ((A.tensor.piece (n : ℤ)).LocalGeneratorsData.{t, t, t, t})
```

**`Stacks.SheafOfModules.isFiniteType_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerLocalGenerators.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerLocalGenerators.lean#L173). The attribute's comment: “tensor powers of a module of finite type”.

> Each tensor power of a sheaf of modules of finite type on a ringed space is of finite
> type.

```lean
theorem isFiniteType_tensorPower [hF : _root_.SheafOfModules.IsFiniteType.{t, t, t} F] (n : ℕ) :
    _root_.SheafOfModules.IsFiniteType.{t, t, t} (A.tensor.piece (n : ℤ))
```

**`Stacks.SheafOfModules.isQuasicoherent_tensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerPresentation.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerPresentation.lean#L548). The attribute's comment: “tensor powers of a quasi-coherent module”.

> **Each tensor power of a quasi-coherent sheaf of modules on a ringed space is
> quasi-coherent.** This is clause (5) of Stacks Tag 01CK for the tensor powers. A presentation of
> `F` over an open presents `Tⁿ(F)` over that same open, by
> `Stacks.SheafOfModules.nonempty_presentation_tensorPower_over`, so the covering family which
> presents `F` presents each tensor power too.

```lean
theorem isQuasicoherent_tensorPower {X : AlgebraicGeometry.RingedSpace.{t, t}}
    (F : _root_.SheafOfModules.{t} (structureSheafRing X)) [F.IsQuasicoherent]
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier) F) (n : ℕ) :
    (A.tensor.piece (n : ℤ)).IsQuasicoherent
```

**`Stacks.SheafOfModules.isQuasicoherent_exteriorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ConstantRank.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/Reflexive/ConstantRank.lean#L123). The attribute's comment: “exterior powers of a quasi-coherent module”.

> **Each exterior power of a quasi-coherent sheaf of modules on a ringed space is
> quasi-coherent.** A presentation of the module over an open presents every exterior power of it
> over that same open, by `Stacks.SheafOfModules.nonempty_presentation_exteriorPower_over`, so the
> covering family which presents the module presents the exterior power too.

```lean
theorem isQuasicoherent_exteriorPower {X : RingedSpace.{u, u}}
    (F : _root_.SheafOfModules.{u} (structureSheafRing X)) [F.IsQuasicoherent]
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier) F) (n : ℕ) :
    (A.exteriorPower n).IsQuasicoherent
```

**`Stacks.SymGraded.isQuasicoherentPieces_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SymAlgebraQcohPieces/Basic.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SymAlgebraQcohPieces/Basic.lean#L408). The attribute's comment: “symmetric powers of a quasi-coherent module, at the encoding Stacks.SymGraded.schemeSymAlgebra”.

> **Every homogeneous piece of `Sym(E)` is quasi-coherent, for `E` a quasi-coherent module on
> an arbitrary scheme.** This discharges the hypothesis
> `Stacks.SymGraded.IsQuasicoherentPieces` of `Stacks.SymGraded.schemeSheafGradedAlgebra` and of
> `Stacks.SymGraded.schemeProjectiveBundle` for a quasi-coherent module.

```lean
theorem isQuasicoherentPieces_of_isQuasicoherent {X : Scheme.{u}} (E : X.Modules)
    [E.IsQuasicoherent] : IsQuasicoherentPieces E
```

**`Stacks.SliceAlgebra.isQuasicoherent_sheafifiedSymmetricPiece`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SymmetricFree/Presentation.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SymmetricFree/Presentation.lean#L157). The attribute's comment: “symmetric powers of a quasi-coherent module”.

> **Symmetric powers of a quasi-coherent module are quasi-coherent.** For a quasi-coherent sheaf
> of modules `F` on a scheme `X` and `n : ℕ`, the degree-`n` piece of the symmetric algebra of `F` is
> quasi-coherent.

```lean
theorem SliceAlgebra.isQuasicoherent_sheafifiedSymmetricPiece (X : Scheme.{u})
    (F : X.Modules) [F.IsQuasicoherent] (n : ℕ) :
    ((sheafifiedSymmetricAlgebra (Opens.grothendieckTopology ↥X) F).piece
      (n : ℤ)).IsQuasicoherent
```

## Tag 01CL, a lemma

[Tag 01CL](https://stacks.math.columbia.edu/tag/01CL) in the Stacks Project.

**`Stacks.SheafOfModules.isLocallyFree_symmetricAlgebraSheaf_of_isLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeAlgebras.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeAlgebras.lean#L147). The attribute's comment: “the symmetric algebra of a locally free module sheaf is locally free”. References: SGA 3 XXII (5.3.0), “partial”.

> **The symmetric algebra of a locally free sheaf of modules is locally free.** The covering
> family is the one that trivialises `F`; no degree needs a smaller object of the site, because
> `Stacks.SheafOfModules.symmetricPowerOverFreeIsoOfIsoFree` trivialises every degree over that
> same object.

```lean
theorem isLocallyFree_symmetricAlgebraSheaf_of_isLocallyFree :
    A.symmetricAlgebraSheaf.IsLocallyFree
```

**`Stacks.SheafOfModules.isLocallyFree_exteriorAlgebraSheaf_of_isLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeAlgebras.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeAlgebras.lean#L162). The attribute's comment: “the exterior algebra of a locally free module sheaf is locally free”.

> **The exterior algebra of a locally free sheaf of modules is locally free.** The covering
> family is the one that trivialises `F`, and
> `Stacks.SheafOfModules.exteriorPowerOverFreeIsoOfIsoFree` trivialises every degree over the same
> object of the site.

```lean
theorem isLocallyFree_exteriorAlgebraSheaf_of_isLocallyFree :
    A.exteriorAlgebraSheaf.IsLocallyFree
```

**`Stacks.SheafOfModules.isLocallyFree_tensorAlgebraSheaf_of_isLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeAlgebras.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFreeAlgebras.lean#L178). The attribute's comment: “the tensor algebra of a locally free module sheaf is locally free”.

> **The tensor algebra of a locally free sheaf of modules is locally free.** The covering
> family is the one that trivialises `F`, and
> `Stacks.SheafOfModules.exists_nonempty_iso_free_tensorPowerOver` trivialises every degree over
> the same object of the site.

```lean
theorem isLocallyFree_tensorAlgebraSheaf_of_isLocallyFree :
    A.tensorAlgebraSheaf.IsLocallyFree
```

**`Stacks.SheafOfModules.isQuasicoherent_symmetricAlgebraSheaf_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean, line 779](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean#L779). The attribute's comment: “the symmetric algebra of a quasi-coherent module sheaf is quasi-coherent”.

> **The symmetric algebra of a quasi-coherent sheaf of modules on a ringed space is
> quasi-coherent.** The covering family is the one that presents `F`; no degree needs a smaller
> open, because
> `Stacks.SheafOfModules.nonempty_presentation_symmetricPower_over` presents every degree over
> that same open.

```lean
theorem isQuasicoherent_symmetricAlgebraSheaf_of_isQuasicoherent :
    A.symmetricAlgebraSheaf.IsQuasicoherent
```

**`Stacks.SheafOfModules.isQuasicoherent_exteriorAlgebraSheaf_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean, line 788](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/QuasicoherentAlgebras.lean#L788). The attribute's comment: “the exterior algebra of a quasi-coherent module sheaf is quasi-coherent”.

> **The exterior algebra of a quasi-coherent sheaf of modules on a ringed space is
> quasi-coherent.**

```lean
theorem isQuasicoherent_exteriorAlgebraSheaf_of_isQuasicoherent :
    A.exteriorAlgebraSheaf.IsQuasicoherent
```

**`Stacks.SheafOfModules.isQuasicoherent_tensorAlgebraSheaf_of_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerPresentation.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPowerPresentation.lean#L569). The attribute's comment: “the tensor algebra of a quasi-coherent module sheaf is quasi-coherent”.

> **The tensor algebra of a quasi-coherent sheaf of modules on a ringed space is
> quasi-coherent.** This is the tensor assertion of Stacks Tag 01CL. The covering family is the one
> that presents `F`; no degree needs a smaller open, because
> `Stacks.SheafOfModules.nonempty_presentation_tensorPower_over` presents every degree over that
> same open.

```lean
theorem isQuasicoherent_tensorAlgebraSheaf_of_isQuasicoherent
    {X : AlgebraicGeometry.RingedSpace.{t, t}}
    (F : _root_.SheafOfModules.{t} (structureSheafRing X)) [F.IsQuasicoherent]
    (A : _root_.SheafOfModules.TensorExteriorSymmetricAlgebras
      (Opens.grothendieckTopology X.carrier) F) :
    A.tensorAlgebraSheaf.IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.21, Tag 01CF](https://stacks.math.columbia.edu/tag/01CF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
