---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_closedImmersion_algebraization_of_isPullback_holds, AlgebraicGeometry.exists_finite_algebraization_of_adicFiniteSystem_holds, AlgebraicGeometry.existsUnique_algebraization_adicBaseChangeMap_holds, Stacks.GrothendieckAlgebraization.exists_isProper_isAmple_algebraization
statement: formalized
proof: formalized
---

# 30.28 Grothendieck's algebraization theorem

Section 30.28 of the Stacks Project, [Tag 0898](https://stacks.math.columbia.edu/tag/0898). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0899, a lemma

[Tag 0899](https://stacks.math.columbia.edu/tag/0899) in the Stacks Project.

**`AlgebraicGeometry.exists_closedImmersion_algebraization_of_isPullback_holds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicFiniteAlgebraizationTags.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicFiniteAlgebraizationTags.lean#L163). The attribute's comment: “at the source's hypotheses and with no further input: A Noetherian and I-adically complete, f : X -> Spec A separated of finite type (IsSeparated, LocallyOfFiniteType and QuasiCompact), a system j n : Z n -> X n with cartesian transition squares whose j 0 is a closed immersion (source hypothesis 1) and whose Z 0 -> S 0 is proper (source hypothesis 2), concluding a closed immersion g : W -> X with W proper over Spec A recovering the system by base change. The halg binder of AlgebraicGeometry.exists\_closedImmersion\_algebraization\_of\_isPullback is discharged here, by AlgebraicGeometry.adicFiniteSystemAlgebraization\_of\_adicFiniteAlgebraAlgebraization at AlgebraicGeometry.adicFiniteAlgebraAlgebraization\_holds, and its hrig binder by AlgebraicGeometry.adicMorphismRigidity”.

> **Algebraization of a cartesian system of closed immersions over the adic thickenings.** Let
> `A` be a Noetherian ring complete with respect to an ideal `I`, write `S = Spec A` and
> `Sₙ = Spec (A / Iⁿ)`, and let `f : X ⟶ S` be separated of finite type; put `Xₙ = X ×_S Sₙ`. Given a
> system of morphisms `jₙ : Zₙ ⟶ Xₙ` with transition maps making every square over `Xₙ ⟶ Xₙ₊₁`
> cartesian, with `j 0 : Z₀ ⟶ X₀` a closed immersion and `Z₀ ⟶ S₀` proper, there is a closed
> immersion `g : W ⟶ X` with `W` proper over `S` recovering the system by base change.

```lean
public theorem exists_closedImmersion_algebraization_of_isPullback_holds
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (hcomplete : IsAdicComplete I A) {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (Z : ℕ → Scheme.{u}) (j : ∀ n, Z n ⟶ adicBaseChange A I f n) (t : ∀ n, Z n ⟶ Z (n + 1))
    (hcart : ∀ n, IsPullback (t n) (j n) (j (n + 1)) (adicBaseChangeSucc A I f n))
    (hclosed : IsClosedImmersion (j 0))
    (hproper : IsProper (j 0 ≫ pullback.snd f (adicThickeningι A I 0))) :
    ∃ (W : Scheme.{u}) (g : W ⟶ X) (k : ∀ n, Z n ⟶ W),
      IsClosedImmersion g ∧ IsProper (g ≫ f) ∧
      (∀ n, IsPullback (k n) (j n ≫ pullback.snd f (adicThickeningι A I n)) (g ≫ f)
        (adicThickeningι A I n)) ∧
      (∀ n, k n ≫ g = j n ≫ pullback.fst f (adicThickeningι A I n)) ∧
      ∀ n, t n ≫ k (n + 1) = k n
```

## Tag 09ZT, a lemma

[Tag 09ZT](https://stacks.math.columbia.edu/tag/09ZT) in the Stacks Project.

**`AlgebraicGeometry.exists_finite_algebraization_of_adicFiniteSystem_holds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicFiniteAlgebraizationTags.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicFiniteAlgebraizationTags.lean#L97). The attribute's comment: “at the source's hypotheses and with no further input: A Noetherian and I-adically complete, f : X -> Spec A separated of finite type (IsSeparated, LocallyOfFiniteType and QuasiCompact), a system (Y n) of schemes over the adic thickenings with cartesian transition squares, every Y n -> X n finite (source hypothesis 1) and Y 0 -> S 0 proper (source hypothesis 2), concluding the finite algebraization a : Z -> X proper over Spec A with every Y n the fibre product Z x\_S S n. The halg binder of AlgebraicGeometry.exists\_finite\_algebraization\_of\_adicFiniteSystem is discharged here, by AlgebraicGeometry.adicFiniteAlgebraAlgebraization\_holds”.

> **Algebraization of a cartesian system of finite schemes over the adic thickenings.** Let `A`
> be a Noetherian ring complete with respect to an ideal `I`, write `S = Spec A` and
> `Sₙ = Spec (A / Iⁿ)`, and let `f : X ⟶ S` be separated of finite type; put `Xₙ = X ×_S Sₙ`. Let
> `(Yₙ)` be a system of schemes over the `Xₙ` whose squares over the transitions `Xₙ ⟶ Xₙ₊₁` are
> cartesian, with every `Yₙ ⟶ Xₙ` finite and `Y₀ ⟶ S₀` proper. Then there is a finite morphism
> `a : Z ⟶ X` which is proper over `S` and maps `kₙ : Yₙ ⟶ Z` over `X` exhibiting every `Yₙ` as the
> fibre product `Z ×_S Sₙ`.

```lean
public theorem exists_finite_algebraization_of_adicFiniteSystem_holds
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    (Y : ℕ → Scheme.{u}) (y : ∀ n, Y n ⟶ adicBaseChange A I f n)
    (t : ∀ n, Y n ⟶ Y (n + 1))
    (hcart : ∀ n, IsPullback (t n) (y n) (y (n + 1)) (adicBaseChangeSucc A I f n))
    (hfin : ∀ n, IsFinite (y n))
    (hproper : IsProper (y 0 ≫ pullback.snd f (adicThickeningι A I 0))) :
    ∃ (Z : Scheme.{u}) (a : Z ⟶ X), IsFinite a ∧ IsProper (a ≫ f) ∧
      ∃ k : ∀ n, Y n ⟶ Z,
        (∀ n, IsPullback (k n) (y n ≫ pullback.snd f (adicThickeningι A I n)) (a ≫ f)
          (adicThickeningι A I n)) ∧
        ∀ n, k n ≫ a = y n ≫ pullback.fst f (adicThickeningι A I n)
```

## Tag 0A42, a lemma

[Tag 0A42](https://stacks.math.columbia.edu/tag/0A42) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_algebraization_adicBaseChangeMap_holds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicFiniteAlgebraizationTags.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/CompletionProper/AdicFiniteAlgebraizationTags.lean#L128). The attribute's comment: “at the source's hypotheses and with no further input: A Noetherian and I-adically complete, fX : X -> Spec A proper (source hypothesis 1), fY : Y -> Spec A separated of finite type (source hypothesis 2), and a compatible system of morphisms over the adic thickenings, concluding that it comes from a unique morphism X -> Y over Spec A. The halg and hrig binders of AlgebraicGeometry.existsUnique\_algebraization\_adicBaseChangeMap are discharged here, by AlgebraicGeometry.adicFiniteAlgebraization\_holds and Stacks.AdicClosedSubschemeRigidity.adicRigidity”.

> **Algebraization of a compatible system of morphisms over the adic thickenings.** Let `A` be a
> Noetherian ring complete with respect to an ideal `I`, write `S = Spec A` and `Sₙ = Spec (A / Iⁿ)`,
> and let `fX : X ⟶ S` be proper and `fY : Y ⟶ S` separated of finite type. A compatible system of
> morphisms `gₙ : Xₙ ⟶ Yₙ` over `Sₙ` comes from a unique morphism `g : X ⟶ Y` over `S` whose base
> change to each `Sₙ` is `gₙ`.

```lean
public theorem existsUnique_algebraization_adicBaseChangeMap_holds
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (hcomplete : IsAdicComplete I A) {X Y : Scheme.{u}}
    (fX : X ⟶ Spec (.of A)) (fY : Y ⟶ Spec (.of A))
    [IsProper fX] [IsSeparated fY] [LocallyOfFiniteType fY] [QuasiCompact fY]
    (g : ∀ n, adicBaseChange A I fX n ⟶ adicBaseChange A I fY n)
    (g_over : ∀ n, g n ≫ pullback.snd fY (adicThickeningι A I n) =
      pullback.snd fX (adicThickeningι A I n))
    (g_compatible : ∀ n, adicBaseChangeSucc A I fX n ≫ g (n + 1) =
      g n ≫ adicBaseChangeSucc A I fY n) :
    ∃! algebraization : {h : X ⟶ Y // h ≫ fY = fX},
      ∀ n, adicBaseChangeMap A I algebraization.1 algebraization.2 n = g n
```

## Tag 089A, a theorem

[Tag 089A](https://stacks.math.columbia.edu/tag/089A) in the Stacks Project.

**`Stacks.GrothendieckAlgebraization.exists_isProper_isAmple_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckAlgebraization.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/GrothendieckAlgebraization.lean#L67).

> **Grothendieck's algebraization theorem, [Stacks, Tag 089A].**
>
> Let `A` be a Noetherian ring complete with respect to an ideal `I`, let `Xₙ` be a tower of
> schemes over the thickenings `Sₙ = Spec (A / Iⁿ⁺¹)` with transitions `iₙ : Xₙ ⟶ Xₙ₊₁` whose squares
> over `Sₙ ⟶ Sₙ₊₁` are cartesian, and let `ℒₙ` be invertible modules on the `Xₙ` with isomorphisms
> `φₙ : iₙ^* ℒₙ₊₁ ≅ ℒₙ`. If `X₀ ⟶ S₀` is proper and `ℒ₀` is ample on `X₀`, then there are a proper
> morphism `fX : X ⟶ Spec A`, an ample invertible `𝒪_X`-module `ℒ`, morphisms `kₙ : Xₙ ⟶ X` with
> `iₙ ≫ kₙ₊₁ = kₙ` exhibiting every `Xₙ` as `X ×_{Spec A} Sₙ`, and isomorphisms `ℒₙ ≅ ℒ|_{Xₙ}`
> compatible with the `φₙ`.

```lean
public theorem exists_isProper_isAmple_algebraization (A : Type u) [CommRing A]
    [IsNoetherianRing A] (I : Ideal A) [IsAdicComplete I A] {Xn : ℕ → Scheme.{u}}
    (q : ∀ n, Xn n ⟶ adicThickening A I n) (i : ∀ n, Xn n ⟶ Xn (n + 1))
    (hcart : ∀ n, IsPullback (i n) (q n) (q (n + 1)) (adicThickeningSucc A I n))
    (L : ∀ n, (Xn n).Modules) (hL : ∀ n, IsInvertibleModule (Xn n) (L n))
    (φ : ∀ n, (Scheme.Modules.pullback (i n)).obj (L (n + 1)) ≅ L n)
    (hproper : IsProper (q 0))
    (hample : letI := hL 0; IsAmple (Xn 0) (L 0)) :
    ∃ (X : Scheme.{u}) (fX : X ⟶ Spec (.of A)), IsProper fX ∧
      ∃ (M : X.Modules) (hM : IsInvertibleModule X M), @IsAmple X M hM ∧
        ∃ (k : ∀ n, Xn n ⟶ X) (hk : ∀ n, i n ≫ k (n + 1) = k n),
          (∀ n, IsPullback (k n) (q n) fX (adicThickeningι A I n)) ∧
          ∃ e : ∀ n, L n ≅ (Scheme.Modules.pullback (k n)).obj M,
            ∀ n, (φ n).hom ≫ (e n).hom =
              (Scheme.Modules.pullback (i n)).map (e (n + 1)).hom ≫
                (Scheme.Modules.pullbackComp (i n) (k (n + 1))).hom.app M ≫
                  (Scheme.Modules.pullbackCongr (hk n)).hom.app M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.28, Tag 0898](https://stacks.math.columbia.edu/tag/0898)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
