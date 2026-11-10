---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.FieldExtensionBaseChange.isIso_smallEtaleDerivedBaseChangeAb_of_stalks, Stacks.EtaleCohomology.bijective_etaleCohomology_pullback_of_isSepClosed, Stacks.EtaleCohomology.isIso_derivedUnit_baseChange_of_isSepClosed, Stacks.EtaleCohomology.FirstFailureFunctionField.functionFieldFailure_of_not_baseChangeHolds
statement: formalized
proof: formalized
---

# 59.90 Applications of smooth base change

Section 59.90 of the Stacks Project, [Tag 0F0A](https://stacks.math.columbia.edu/tag/0F0A). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F1C, a lemma

[Tag 0F1C](https://stacks.math.columbia.edu/tag/0F1C) in the Stacks Project.

**`Stacks.EtaleCohomology.FieldExtensionBaseChange.isIso_smallEtaleDerivedBaseChangeAb_of_stalks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/FieldExtensionBaseChangeTheorem.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/FieldExtensionBaseChangeTheorem.lean#L65). The attribute's comment: “the base change map `(S_L ⟶ S)⁻¹ Rg_* E ⟶ Rg_{L,*} E_L` is an isomorphism”.

> **Direct images commute with extension of the base field** ([Stacks, Tag 0F1C]). Let `L/K`
> be an extension of fields, let `g : T ⟶ S` be a quasi-compact and quasi-separated morphism of
> schemes over `K`, and let `g_L : T_L ⟶ S_L` be its base change to `Spec L`, with
> `S_L = Spec L ×_K S` and `T_L = Spec L ×_K T`. Let `E ∈ D⁺(T_étale)` have cohomology sheaves whose
> stalks are torsion of orders invertible in `K`: every element of the stalk of `H^q(E)` at every
> geometric point of `T` is killed by a positive integer invertible in `K`. Let `E_L` be the
> pullback of `E` to `(T_L)_étale`. Then `Rg_{L,*} E_L` is the pullback of `Rg_* E` to `S_L`: the
> base change map `(S_L ⟶ S)⁻¹ Rg_* E ⟶ Rg_{L,*} E_L` is an isomorphism.

```lean
theorem isIso_smallEtaleDerivedBaseChangeAb_of_stalks
    (E : DerivedCategory.Plus (Sheaf (smallEtaleTopology T) Ab.{u + 1}))
    (hE : ∀ (q : ℤ) (t : GeometricPoint T)
      (a : ↑((smallEtaleStalkAb t.hom).obj ((DerivedCategory.Plus.homologyFunctor _ q).obj E))),
      ∃ n : ℕ, 0 < n ∧ IsUnit (n : K) ∧ n • a = 0) :
    IsIso ((smallEtaleDerivedBaseChangeAb (pullback.snd _ sS) g
      (baseChangeMap (Spec.map (CommRingCat.ofHom (algebraMap K L))) sS sT g hg)
      (pullback.snd _ sT) (baseChangeMap_snd _ sS sT g hg)).app E)
```

## Tag 0F0B, a lemma

[Tag 0F0B](https://stacks.math.columbia.edu/tag/0F0B) in the Stacks Project.

**`Stacks.EtaleCohomology.bijective_etaleCohomology_pullback_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/SeparablyClosedFieldInvariance.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/SeparablyClosedFieldInvariance.lean#L71). The attribute's comment: “(1): H^q(X, E) ⟶ H^q(X\_K, E|\_\{X\_K}) is an isomorphism for K/k separably closed”. References: SGA 4 XII (5.4), “special case”; SGA 4 XVI (1.6), “Abelian L-torsion clause”; SGA 4½ Arcata (5.3.3), “special case”; SGA 4½ Th finitude (3.9), “more general”.

> **[Stacks, Tag 0F0B] (1).** Let `K/k` be an extension of separably closed fields, `X` a
> quasi-compact and quasi-separated scheme over `k`, `p : X_K ⟶ X` its base change to `K` and `E` in
> `D⁺(X_étale)` whose cohomology sheaves have stalks which are torsion of orders invertible in `k`.
> Then for every `q` the restriction map `H^q_ét(X, E) ⟶ H^q_ét(X_K, E|_{X_K})` is bijective. Here
> `H^q_ét(X, E)` is the group of morphisms in `D⁺(X_étale)` from the constant sheaf `ℤ` placed in
> degree `-q` to `E`, and restriction is the derived pullback along `p` followed by the
> identification of the pullback of `ℤ_X` with `ℤ_{X_K}`.

```lean
theorem bijective_etaleCohomology_pullback_of_isSepClosed
    {k K : Type u} [Field k] [Field K] [Algebra k K] [IsSepClosed k] [IsSepClosed K]
    {X XK : Scheme.{u}} (f : X ⟶ Spec (.of k)) [QuasiCompact f] [QuasiSeparated f]
    (p : XK ⟶ X) (fK : XK ⟶ Spec (.of K))
    (sq : IsPullback p fK f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
    (E : DerivedCategory.Plus (Sheaf (smallEtaleTopology X) Ab.{u + 1}))
    (hE : ∀ q : ℤ, HasTorsionOrdersInvertibleOn (Spec (.of k))
      ((DerivedCategory.Plus.homologyFunctor (Sheaf (smallEtaleTopology X) Ab.{u + 1}) q).obj E))
    (q : ℤ) :
    Function.Bijective
      (fun φ : (DerivedCategory.Plus.singleFunctor _ (-q)).obj (constantZ X) ⟶ E ↦
        (singleConstantZPullbackIso p (-q)).hom ≫
          (smallEtalePullbackAb p).rightDerivedFunctorPlus.map φ)
```

**`Stacks.EtaleCohomology.isIso_derivedUnit_baseChange_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/SeparablyClosedFieldInvariance.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/SeparablyClosedFieldInvariance.lean#L93). The attribute's comment: “(2): E ⟶ R(X\_K → X)\_* E|\_\{X\_K} is an isomorphism for K/k separably closed”. References: SGA 4 XVI (1.6), “partial”.

> **[Stacks, Tag 0F0B] (2).** Let `K/k` be an extension of separably closed fields, `X` a scheme
> over `k`, `p : X_K ⟶ X` its base change to `K` and `E` in `D⁺(X_étale)` whose cohomology sheaves
> have stalks which are torsion of orders invertible in `k`. Then `E ⟶ Rp_*(E|_{X_K})`, the unit of
> the derived adjunction `p⁻¹ ⊣ Rp_*` at `E`, is an isomorphism. The source assumes `X`
> quasi-compact and quasi-separated; the statement holds without it.

```lean
theorem isIso_derivedUnit_baseChange_of_isSepClosed
    {k K : Type u} [Field k] [Field K] [Algebra k K] [IsSepClosed k] [IsSepClosed K]
    {X XK : Scheme.{u}} (f : X ⟶ Spec (.of k)) (p : XK ⟶ X) (fK : XK ⟶ Spec (.of K))
    (sq : IsPullback p fK f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
    (E : DerivedCategory.Plus (Sheaf (smallEtaleTopology X) Ab.{u + 1}))
    (hE : ∀ q : ℤ, HasTorsionOrdersInvertibleOn (Spec (.of k))
      ((DerivedCategory.Plus.homologyFunctor (Sheaf (smallEtaleTopology X) Ab.{u + 1}) q).obj E)) :
    IsIso ((smallEtaleAdjunctionAb p).rightDerivedFunctorPlus.unit.app E)
```

## Tag 0F1D, a lemma

[Tag 0F1D](https://stacks.math.columbia.edu/tag/0F1D) in the Stacks Project.

**`Stacks.EtaleCohomology.FirstFailureFunctionField.functionFieldFailure_of_not_baseChangeHolds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/FirstFailureOverFunctionField.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SmoothBaseChange/FirstFailureOverFunctionField.lean#L78).

> **Stacks Project, Tag 0F1D.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], assume `n`
> is invertible on `S`, `BC(f, n, q)` holds and `BC(f, n, q + 1)` does not. Then there are
> cartesian squares
>
> ```
> X  ←--  X'  ←-h-  Y
> |f      |         |
> S  ←--  S'  ←---  Spec K
> ```
>
> where `S'` is affine, integral and normal with algebraically closed function field `K = K(S')`,
> the bottom right arrow is the canonical morphism from the spectrum of the function field, and
> there is an integer `d ∣ n` with `R^{q+1} h_*(ℤ/dℤ)` nonzero
> (`Stacks.EtaleCohomology.FirstFailureFunctionField.FunctionFieldFailure`).

```lean
public theorem functionFieldFailure_of_not_baseChangeHolds {X S : Scheme.{u}} (f : X ⟶ S)
    (n : ℤ) (q : ℕ) (hn : IsUnit (n : Γ(S, ⊤))) (hprev : BaseChangeHolds f n (q : ℤ))
    (hfail : ¬ BaseChangeHolds f n ((q : ℤ) + 1)) : FunctionFieldFailure f n (q + 1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.90, Tag 0F0A](https://stacks.math.columbia.edu/tag/0F0A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
