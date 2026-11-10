---
declaration: section
origin: cited
lean: IsLocalRing.exists_henselization, IsLocalRing.exists_strictHenselization, Stacks.StrictHenselization.exists_isStrictHenselization, IsLocalRing.IsHenselization, IsLocalRing.IsHenselization.exists_strictHenselization_iUnion_finiteEtale, existsUnique_ringHom_to_henselian_of_etale, HenselianLocalRing.indEtaleAlgHom, HenselianLocalRing.isLocalHom_indEtaleAlgHom
statement: formalized
proof: formalized
---

# 10.155 Henselization and strict henselization

Section 10.155 of the Stacks Project, [Tag 0BSK](https://stacks.math.columbia.edu/tag/0BSK). 13 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04GN, a lemma

[Tag 04GN](https://stacks.math.columbia.edu/tag/04GN) in the Stacks Project.

**`IsLocalRing.exists_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/Existence.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Henselization/Existence.lean#L709). The attribute's comment: “The lemma's preamble, a local ring map `R → Rh`, is the `Algebra R Rh`, `IsLocalRing Rh` and `IsLocalHom (algebraMap R Rh)` binders; the four conjuncts are its items (1)–(4). `Rh` being a filtered colimit of étale `R`-algebras is `(CommAlgCat.etale R).ind`, i.e. `Rh` is ind-étale over `R`; `𝔪 Rh` is `Ideal.map`; and `κ = Rh/𝔪 Rh` is bijectivity of the canonical `IsLocalRing.ResidueField.map`. See the module docstring.”. References: EGA IV (18.6.6), “(i), part of (iii)”; SGA 4 VIII (4.1), “henselization”; SGA 4 VIII (4.1), “henselization”.

> **Existence of the henselization of a local ring** (Stacks 04GN). For a local ring
> `(R, 𝔪, κ)` there is a local ring map `R → Rh` such that (1) `Rh` is henselian, (2) `Rh` is a
> filtered colimit of étale `R`-algebras, (3) `𝔪 Rh` is the maximal ideal of `Rh`, and (4) the
> residue field of `Rh` is `κ`.

```lean
public theorem IsLocalRing.exists_henselization (R : Type u) [CommRing R] [IsLocalRing R] :
    ∃ (Rh : Type u) (_ : CommRing Rh) (_ : Algebra R Rh) (_ : IsLocalRing Rh)
      (_ : IsLocalHom (algebraMap R Rh)),
      HenselianLocalRing Rh ∧
      (CommAlgCat.etale.{u} R).ind.{u} (CommAlgCat.of R Rh) ∧
      (maximalIdeal R).map (algebraMap R Rh) = maximalIdeal Rh ∧
      Function.Bijective (ResidueField.map (algebraMap R Rh))
```

## Tag 04GP, a lemma

[Tag 04GP](https://stacks.math.columbia.edu/tag/04GP) in the Stacks Project.

**`IsLocalRing.exists_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/Existence.lean, line 898](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/Existence.lean#L898). The attribute's comment: “The diagram's middle column is a hypothesis: `Rh` is any local ind-étale `R`-algebra with residue field `κ`, which by Lemmas 04GN and 04GS is the henselization; the conclusion produces `Rsh` with the algebra structure over `Rh` and item (1). Strictly henselian is `HenselianLocalRing` plus `IsSepClosed` on the residue field, `Rsh` a filtered colimit of étale `R`-algebras is `(CommAlgCat.etale R).ind`, `𝔪 Rsh` is `Ideal.map`, and `κ^sep = Rsh/𝔪 Rsh` is an isomorphism `κ^sep ≃+* ResidueField Rsh` compatible with the maps out of `R`. See the module docstring.”. References: EGA IV (18.8.8), “(i), part of (iii)”.

> **Existence of the strict henselization of a local ring.** Let `(R, 𝔪, κ)` be a local ring,
> let `κ ⊆ κ^sep` be a separable algebraic closure, and let `Rh` be a local `R`-algebra with
> `R → Rh` local which is a filtered colimit of étale `R`-algebras with residue field `κ` (the
> henselization of `R`). Then there is a commutative diagram `R → Rh → Rsh` over `κ → κ → κ^sep`
> such that (1) `Rh → Rsh` is a local ring map, (2) `Rsh` is strictly henselian, (3) `Rsh` is a
> filtered colimit of étale `R`-algebras, (4) `𝔪 Rsh` is the maximal ideal of `Rsh`, and (5) the
> residue field of `Rsh` is `κ^sep`.

```lean
public theorem IsLocalRing.exists_strictHenselization (R : Type u) [CommRing R] [IsLocalRing R]
    (Rh : Type u) [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh] [IsLocalHom (algebraMap R Rh)]
    (hRh : (CommAlgCat.etale.{u} R).ind.{u} (CommAlgCat.of R Rh))
    (hRhres : Function.Surjective (ResidueField.map (algebraMap R Rh)))
    (κsep : Type u) [Field κsep] [Algebra (ResidueField R) κsep]
    [IsSepClosure (ResidueField R) κsep] :
    ∃ (Rsh : Type u) (_ : CommRing Rsh) (_ : IsLocalRing Rsh) (_ : Algebra R Rsh)
      (_ : Algebra Rh Rsh) (_ : IsScalarTower R Rh Rsh) (_ : IsLocalHom (algebraMap Rh Rsh)),
      HenselianLocalRing Rsh ∧
      IsSepClosed (ResidueField Rsh) ∧
      (CommAlgCat.etale.{u} R).ind.{u} (CommAlgCat.of R Rsh) ∧
      (maximalIdeal R).map (algebraMap R Rsh) = maximalIdeal Rsh ∧
      ∃ e : κsep ≃+* ResidueField Rsh, ∀ x : R,
        e (algebraMap (ResidueField R) κsep (residue R x)) = residue Rsh (algebraMap R Rsh x)
```

**`Stacks.StrictHenselization.exists_isStrictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/ExistenceData.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/ExistenceData.lean#L164). The attribute's comment: “The five properties of the source's conclusion are bundled into the predicate `Stacks.StrictHenselization.IsStrictHenselization`, and the henselization `R^h`, which the sibling statement in `StrictHenselization.Existence` carries as a hypothesis, is produced here by `IsLocalRing.exists_henselization` rather than assumed; so this is the source's existential form. The separable algebraic closure is taken over `(maximalIdeal R).ResidueField`, the spelling `IsStrictHenselization` uses, and may lie in a universe independent of `R`.”. References: EGA IV (18.8.7); EGA IV (18.8.8); SGA 4 VIII (4.4).

> **Existence of the strict henselization** (Stacks 04GP). A local ring `(R, 𝔪, κ)` together
> with a separable algebraic closure `κ ⊆ κ^sep` of its residue field admits a local `R`-algebra
> `R^{sh}` which is a strict henselization of `R` with respect to `κ ⊆ κ^sep`, that is: it is
> strictly henselian, `R → R^{sh}` is a local ring map realizing `R^{sh}` as a filtered colimit of
> étale `R`-algebras, `𝔪 R^{sh}` is the maximal ideal of `R^{sh}`, and the residue field of
> `R^{sh}` is identified with `κ^sep` compatibly with `κ ⊆ κ^sep`.

```lean
public theorem exists_isStrictHenselization (R : Type u) [CommRing R] [IsLocalRing R]
    (κ : Type v) [Field κ] [Algebra (maximalIdeal R).ResidueField κ]
    [IsSepClosure (maximalIdeal R).ResidueField κ] :
    ∃ (Rsh : Type u) (_ : CommRing Rsh) (_ : IsLocalRing Rsh) (_ : Algebra R Rsh),
      Nonempty (IsStrictHenselization R κ Rsh)
```

## Tag 04GQ, a definition

[Tag 04GQ](https://stacks.math.columbia.edu/tag/04GQ) in the Stacks Project.

**`IsLocalRing.IsHenselization`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/Defs.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Henselization/Defs.lean#L169). The attribute's comment: “One predicate for the source's three items: part (1) is `IsHenselization R (ResidueField R) Rh`, part (2) is `IsHenselization R κsep Rsh` for `κ ⊆ κ^sep` a separable algebraic closure, and part (3) is the isomorphism invariance of the three fields, which by Lemma 08HT makes them equivalent to being isomorphic to a ring Lemma 04GP constructs. `Rh` being a filtered colimit of étale `R`-algebras is `(CommAlgCat.etale R).ind`, as in Lemmas 04GN and 04GP, and the residue field condition is item (5) of Lemma 04GP. Locality of `R → Rh` and `𝔪 Rh = 𝔪_{Rh}` are consequences, not fields. See the module docstring.”. References: EGA IV (18.8.7).

> **Henselization of a local ring** (Stacks 04GQ). Let `(R, 𝔪, κ)` be a local ring and let
> `κ ⊆ L` be an extension of its residue field. A local `R`-algebra `Rh` is a *henselization of `R`
> with residue field `L`* if `Rh` is henselian, is a filtered colimit of étale `R`-algebras, and has
> residue field `L` compatibly with `κ ⊆ L`. For `L = κ` this is the henselization `R → R^h` of
> Lemma 04GN, and for `L = κ^sep` a separable algebraic closure of `κ` it is a strict henselization
> `R → R^{sh}` of `R` with respect to `κ ⊆ κ^sep`, in the sense of Lemma 04GP; by Lemma 08HT such an
> `Rh` is unique up to a unique `R`-algebra isomorphism over `L`.

```lean
public class IsLocalRing.IsHenselization (R : Type u) [CommRing R] [IsLocalRing R]
    (L : Type v) [Field L] [Algebra (ResidueField R) L]
    (Rh : Type w) [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh] : Prop
```

## Tag 0BSL, a remark

[Tag 0BSL](https://stacks.math.columbia.edu/tag/0BSL) in the Stacks Project.

**`IsLocalRing.IsHenselization.exists_strictHenselization_iUnion_finiteEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/OfHenselization.lean, line 604](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/OfHenselization.lean#L604). The attribute's comment: “The rings `R^h(κ')` are local `Rh`-algebras `A κ'` with injective embeddings `ι` into `Rsh` exhausting it, which is the union of the source. The transition maps are pinned as the unique maps compatible with the inclusions of residue fields, and each `A κ'` is unique up to a unique isomorphism inducing the identity of `κ'`. That `Rsh` is the strict henselization is `IsHenselization` over `Rh` and over `R` with residue field `κsep`.”.

> **The strict henselization as a union of finite étale extensions of the henselization**
> (Stacks 0BSL). Let `R → Rh` be a henselization of the local ring `R` and let `κsep` be a separable
> algebraic closure of the residue field `κ` of `R`, identified with that of `Rh` by `e`. For every
> finite subextension `κ ⊆ κ' ⊆ κsep` there is a finite étale local extension `Rh ⊆ Rh(κ')` with
> residue field extension `κ ⊆ κ'`, unique up to unique isomorphism; for `κ' ⊆ κ''` there is exactly
> one map `Rh(κ') → Rh(κ'')` compatible with `κ' ⊆ κ''`; and the union `Rsh` of the resulting
> directed system is strictly henselian, and is a strict henselization of `Rh` and of `R`.

```lean
theorem IsLocalRing.IsHenselization.exists_strictHenselization_iUnion_finiteEtale
    (R : Type u) [CommRing R] [IsLocalRing R] (Rh : Type u) [CommRing Rh] [IsLocalRing Rh]
    [Algebra R Rh] [IsHenselization R (ResidueField R) Rh] (κsep : Type u) [Field κsep]
    [Algebra (ResidueField R) κsep] [IsSepClosure (ResidueField R) κsep] :
    ∃ e : ResidueField R ≃+* ResidueField Rh,
      (∀ x : R, e (residue R x) = residue Rh (algebraMap R Rh x)) ∧
      letI : Algebra (ResidueField Rh) κsep :=
        ((algebraMap (ResidueField R) κsep).comp e.symm.toRingHom).toAlgebra
      IsSepClosure (ResidueField Rh) κsep ∧
      ∃ (Rsh : Type u) (_ : CommRing Rsh) (_ : IsLocalRing Rsh) (_ : Algebra R Rsh)
        (_ : Algebra Rh Rsh) (_ : IsScalarTower R Rh Rsh)
        (A : ∀ L, FiniteEtaleLocalResidueLift.{u, u, u} R Rh κsep e L)
        (map : ∀ {L L'}, L ≤ L' → A L →ₐ[Rh] A L') (ι : ∀ L, A L →ₐ[Rh] Rsh),
        (∀ L L' (h : L ≤ L') (f : A L →ₐ[Rh] A L'), f = map h ↔
          ∀ a, residue _ (f a) = residueMap (A L) (A L') (IntermediateField.inclusion h)
            (residue _ a)) ∧
        (∀ L, map (le_refl L) = AlgHom.id Rh (A L)) ∧
        (∀ L₁ L₂ L₃ (h₁₂ : L₁ ≤ L₂) (h₂₃ : L₂ ≤ L₃),
          (map h₂₃).comp (map h₁₂) = map (h₁₂.trans h₂₃)) ∧
        (∀ L (B : FiniteEtaleLocalResidueLift.{u, u, t} R Rh κsep e L),
          ∃! f : A L ≃ₐ[Rh] B,
            ∀ a, residue B (f a) = residueMap (A L) B (RingHom.id L) (residue _ a)) ∧
        (∀ L L' (h : L ≤ L') a, ι L' (map h a) = ι L a) ∧
        (∀ L, Function.Injective (ι L)) ∧ (∀ x, ∃ L a, ι L a = x) ∧
        HenselianLocalRing Rsh ∧ IsSepClosed (ResidueField Rsh) ∧
        IsHenselization Rh κsep Rsh ∧ IsHenselization R κsep Rsh
```

## Tag 04GR, a lemma

[Tag 04GR](https://stacks.math.columbia.edu/tag/04GR) in the Stacks Project.

**`existsUnique_ringHom_to_henselian_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean#L543). References: EGA IV (18.5.11), “special case”; EGA IV (18.5.12), “special case”; EGA IV (18.5.17), “affine étale morphisms”; EGA IV (18.6.2); EGA IV (18.8.1), “(a)⇒(c), special case”; EGA IV (18.8.4), “special case”; SGA 1 I (6.2), “special case”; SGA 3 XI (1.11), “special case”; SGA 4 VIII (4.1), “(iii)”.

> **Stacks Tag 04GR.**
> Let `R, S, Sh` be local rings, `R → S` (`rs`) a local ring homomorphism, and
> `S → Sh` (`ssh`) a local ring homomorphism into a henselian local ring `Sh`.
> Let `R → A` be étale and let `q ⊆ A` be a prime lying over the maximal ideal of
> `R` whose induced residue-field map `R/𝔪_R → κ(q)` is bijective. Then there is a
> unique ring homomorphism `f : A → Sh` that is `R`-linear (`f ∘ algebraMap R A =
> ssh ∘ rs`) and satisfies `(maximalIdeal Sh).comap f = q`.

```lean
theorem existsUnique_ringHom_to_henselian_of_etale
    (R S Sh A : Type*)
    [CommRing R] [CommRing S] [CommRing Sh] [CommRing A]
    [IsLocalRing R] [IsLocalRing S]
    [Algebra R A] [Algebra.Etale R A]
    (rs : R →+* S) [IsLocalHom rs]
    (ssh : S →+* Sh) [IsLocalHom ssh] [HenselianLocalRing Sh]
    (q : Ideal A) [q.IsPrime] [q.LiesOver (maximalIdeal R)]
    (hres : Function.Bijective
      (Ideal.ResidueField.map (maximalIdeal R) q (algebraMap R A)
        Ideal.LiesOver.over)) :
    ∃! f : A →+* Sh,
      f.comp (algebraMap R A) = ssh.comp rs ∧ (maximalIdeal Sh).comap f = q
```

## Tag 04GS, a lemma

[Tag 04GS](https://stacks.math.columbia.edu/tag/04GS) in the Stacks Project.

**`HenselianLocalRing.indEtaleAlgHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean#L376). The attribute's comment: “The map of the universal property of `R^h`: the target is an arbitrary henselian local ring `Sh` with `R → Sh` local, since the source's `S` enters only through the composite `R → S → S^h`. Of the henselization `R → Rh` only the two items of Lemma 04GN that the proof uses are assumed — ind-étale, `(CommAlgCat.etale R).ind`, and surjectivity on residue fields. The commutative square is the `R`-algebra structure of the map. `isLocalHom_indEtaleAlgHom` and `indEtaleAlgHom_unique` are its defining property and its uniqueness. See the module docstring.”.

> **The map given by the universal property of the henselization** (Stacks 04GS). Let
> `(R, 𝔪, κ)` be a local ring, let `Rh` be a local `R`-algebra with `R → Rh` local which is a
> filtered colimit of étale `R`-algebras and has residue field `κ`, and let `Sh` be a henselian
> local ring with `R → Sh` local. This is the `R`-algebra map `Rh → Sh` that is a local ring map,
> unique as such by `indEtaleAlgHom_unique`. Applied to the henselizations `Rh = R^h` and
> `Sh = S^h` of a local map of local rings `R → S`, it is the local ring map `R^h → S^h` over
> `R → S` that makes the henselization a functor.

```lean
noncomputable def HenselianLocalRing.indEtaleAlgHom
    {R : Type u} {Rh : Type v} {Sh : Type w} [CommRing R] [CommRing Rh] [CommRing Sh]
    [IsLocalRing R]
    [IsLocalRing Rh] [HenselianLocalRing Sh] [Algebra R Rh] [Algebra R Sh]
    [IsLocalHom (algebraMap R Rh)] [IsLocalHom (algebraMap R Sh)]
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rh)))
    (hres : Function.Surjective (ResidueField.map (algebraMap R Rh))) :
    Rh →ₐ[R] Sh
```

**`HenselianLocalRing.isLocalHom_indEtaleAlgHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean#L390). The attribute's comment: “the defining property of `indEtaleAlgHom`”.

> `HenselianLocalRing.indEtaleAlgHom` is a local ring map.

```lean
public theorem HenselianLocalRing.isLocalHom_indEtaleAlgHom
    {R : Type u} {Rh : Type v} {Sh : Type w} [CommRing R] [CommRing Rh] [CommRing Sh]
    [IsLocalRing R]
    [IsLocalRing Rh] [HenselianLocalRing Sh] [Algebra R Rh] [Algebra R Sh]
    [IsLocalHom (algebraMap R Rh)] [IsLocalHom (algebraMap R Sh)]
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rh)))
    (hres : Function.Surjective (ResidueField.map (algebraMap R Rh))) :
    IsLocalHom (HenselianLocalRing.indEtaleAlgHom (Sh := Sh) hind hres)
```

**`HenselianLocalRing.indEtaleAlgHom_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/HenselizationUniversalProperty.lean#L404). The attribute's comment: “uniqueness of `indEtaleAlgHom`”.

> `HenselianLocalRing.indEtaleAlgHom` is the only local `R`-algebra map `Rh → Sh`.

```lean
public theorem HenselianLocalRing.indEtaleAlgHom_unique
    {R : Type u} {Rh : Type v} {Sh : Type w} [CommRing R] [CommRing Rh] [CommRing Sh]
    [IsLocalRing R]
    [IsLocalRing Rh] [HenselianLocalRing Sh] [Algebra R Rh] [Algebra R Sh]
    [IsLocalHom (algebraMap R Rh)] [IsLocalHom (algebraMap R Sh)]
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rh)))
    (hres : Function.Surjective (ResidueField.map (algebraMap R Rh)))
    (f : Rh →ₐ[R] Sh) (hf : IsLocalHom f) :
    f = HenselianLocalRing.indEtaleAlgHom hind hres
```

## Tag 04GV, a lemma

[Tag 04GV](https://stacks.math.columbia.edu/tag/04GV) in the Stacks Project.

**`IsLocalRing.IsHenselization.isFiltered_etaleNeighborhood_and_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/EtaleNeighborhood.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Henselization/EtaleNeighborhood.lean#L333). The attribute's comment: “Étale neighborhoods `(S, q)` with `κ(p) = κ(q)` are étale `R`-algebras with an augmentation to `κ(p)`, whose kernel is `q`. `canonically` is the characterization of the colimit maps `S → (R_p)^h`: the unique family inducing the identity of `κ(p) = κ((R_p)^h)` on residue fields; the maps `S_q → (R_p)^h` are pinned by extending them along `S → S_q`. The henselization is `IsHenselization` with residue field `κ(p)`.”. References: SGA 4 VIII (4.1), “more general”.

> **The henselization as a colimit of étale neighborhoods** (Stacks 04GV). Let `p` be a prime of
> `R` and let `Rh` be a henselization of `R_p`. The category of étale neighborhoods `(S, q)` of `p`
> with `κ(q) = κ(p)` is filtered, and `Rh` is canonically the colimit of the algebras `S` and also of
> the local rings `S_q`. The canonical maps `S → Rh` are the unique `R`-algebra maps inducing
> `κ(q) = κ(p) ≅ κ(Rh)` on residue fields, and the maps `S_q → Rh` extend them.

```lean
theorem isFiltered_etaleNeighborhood_and_isColimit :
    IsFiltered (EtaleNeighborhood p) ∧
      ∃ ι : EtaleNeighborhood.forget p ⟶ (Functor.const _).obj (CommAlgCat.of R Rh),
        (∀ A x, residue Rh ((ι.app A).hom x) =
          ResidueField.map (algebraMap (Localization.AtPrime p) Rh) (A.hom.hom x)) ∧
        (∀ ι' : EtaleNeighborhood.forget p ⟶ (Functor.const _).obj (CommAlgCat.of R Rh),
          (∀ A x, residue Rh ((ι'.app A).hom x) =
            ResidueField.map (algebraMap (Localization.AtPrime p) Rh) (A.hom.hom x)) → ι' = ι) ∧
        Nonempty (IsColimit (Cocone.mk _ ι)) ∧
        ∃ ιLoc : EtaleNeighborhood.localization p ⟶ (Functor.const _).obj (CommAlgCat.of R Rh),
          (∀ A, (EtaleNeighborhood.toLocalization p).app A ≫ ιLoc.app A = ι.app A) ∧
          Nonempty (IsColimit (Cocone.mk _ ιLoc))
```

## Tag 08HU, a lemma

[Tag 08HU](https://stacks.math.columbia.edu/tag/08HU) in the Stacks Project.

**`IsLocalRing.IsHenselization.exists_unique_prime_isHenselization_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/Henselization/TensorProduct.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/Henselization/TensorProduct.lean#L366). The attribute's comment: “The map `R^h → S^h` of 04GS is pinned as the unique local `R`-algebra map `f` compatible with `R_p → S_q`. The prime is characterized by its two contractions, with uniqueness, and equals `g⁻¹(𝔪_{S^h})` for the map `g` induced by `f`; that `S^h` is the henselization of `(R^h ⊗_R S)_Q` is `IsHenselization` with residue field `κ(Q)`, through an algebra structure extending `g`. All rings share one universe, as `IsHenselization` requires.”.

> **The henselization after a ring map** (Stacks 08HU). Let `R → S` be a ring map and let
> `q ⊆ S` lie over `p ⊆ R`. Let `Rh` and `Sh` be henselizations of `R_p` and `S_q`. The local
> ring map `f : Rh → Sh` of Lemma 04GS (the unique local map over `R_p → S_q`) identifies `Sh` with
> the henselization of `Rh ⊗[R] S` at the unique prime `Q` lying over `𝔪_Rh` and `q`: here `Q` is the
> inverse image of `𝔪_Sh` under the map `g : Rh ⊗[R] S → Sh` induced by `f`, and `Sh` is a
> henselization of `(Rh ⊗[R] S)_Q` through an algebra structure extending `g`.

```lean
theorem exists_unique_prime_isHenselization_tensorProduct [Algebra R Sq] [Algebra Rp Sq]
    [IsScalarTower R S Sq] [IsScalarTower R Rp Sq] [IsHenselization Rp (ResidueField Rp) Rh]
    [Algebra Rp Sh] [IsScalarTower Rp Sq Sh] [IsHenselization Sq (ResidueField Sq) Sh] :
    ∃ f : Rh →ₐ[R] Sh, IsLocalHom f ∧
      f.toRingHom.comp (algebraMap Rp Rh) = algebraMap Rp Sh ∧
      (∀ f' : Rh →ₐ[R] Sh, IsLocalHom f' →
        f'.toRingHom.comp (algebraMap Rp Rh) = algebraMap Rp Sh → f' = f) ∧
      let g : Rh ⊗[R] S →ₐ[R] Sh :=
        Algebra.TensorProduct.lift f (IsScalarTower.toAlgHom R S Sh) fun _ _ => .all _ _
      ∃ (Q : Ideal (Rh ⊗[R] S)) (_ : Q.IsPrime),
        Q.comap (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := Rh) (B := S)) =
          maximalIdeal Rh ∧
        Q.comap (Algebra.TensorProduct.includeRight (R := R) (A := Rh) (B := S)).toRingHom = q ∧
        Q = (maximalIdeal Sh).comap g.toRingHom ∧
        (∀ Q' : Ideal (Rh ⊗[R] S), Q'.IsPrime →
          Q'.comap (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := Rh) (B := S)) =
            maximalIdeal Rh →
          Q'.comap (Algebra.TensorProduct.includeRight (R := R) (A := Rh) (B := S)).toRingHom =
            q → Q' = Q) ∧
        ∃ _ : Algebra (Localization.AtPrime Q) Sh,
          IsLocalHom (algebraMap (Localization.AtPrime Q) Sh) ∧
          IsHenselization (Localization.AtPrime Q) (ResidueField (Localization.AtPrime Q)) Sh ∧
          (algebraMap (Localization.AtPrime Q) Sh).comp
            (algebraMap (Rh ⊗[R] S) (Localization.AtPrime Q)) = g.toRingHom
```

**`StacksDraft.henselization_tensorProduct_at_unique_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HenselizationUniverse/TensorProduct.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HenselizationUniverse/TensorProduct.lean#L287). The attribute's comment: “Stated over six independent universes, as the source requires: the tag's six rings `R`, `R_p`, `R^h`, `S`, `S_q`, `S^h` are unconstrained relative to one another.”.

> **Henselization after a ring map** (Stacks 08HU), at six independent universes. For primes
> `q` over `p`, the canonical local map between henselizations of `R_p` and `S_q` identifies the
> latter with the henselization of `Rh ⊗[R] S` at its unique prime lying over both the maximal
> ideal of `Rh` and `q`. The final equality says that the henselization map is induced by the
> canonical map from the tensor product.
>
> This is the source-strength form of tag 08HU, and the provider of that tag. The weaker
> single-universe statement
> `IsLocalRing.IsHenselization.exists_unique_prime_isHenselization_tensorProduct` pins all six
> rings to one `Type u`; its `@[stacks 08HU]` attribute is dropped in favour of this one. See the
> module docstring.

```lean
theorem henselization_tensorProduct_at_unique_prime
    {R : Type uR} {Rp : Type uRp} {Rh : Type uRh}
    {S : Type uS} {Sq : Type uSq} {Sh : Type uSh}
    [CommRing R] [CommRing S] [Algebra R S]
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p]
    [CommRing Rp] [IsLocalRing Rp] [Algebra R Rp] [IsLocalization.AtPrime Rp p]
    [CommRing Sq] [IsLocalRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q]
    [Algebra R Sq] [Algebra Rp Sq] [IsScalarTower R S Sq] [IsScalarTower R Rp Sq]
    [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh] [Algebra Rp Rh]
    [IsScalarTower R Rp Rh] [IsHenselization Rp (ResidueField Rp) Rh]
    [CommRing Sh] [IsLocalRing Sh] [Algebra R Sh] [Algebra S Sh] [Algebra Rp Sh]
    [Algebra Sq Sh] [IsScalarTower R S Sh] [IsScalarTower S Sq Sh]
    [IsScalarTower Rp Sq Sh] [IsHenselization Sq (ResidueField Sq) Sh] :
    ∃ f : Rh →ₐ[R] Sh,
      IsLocalHom f ∧
      f.toRingHom.comp (algebraMap Rp Rh) = algebraMap Rp Sh ∧
      (∀ f' : Rh →ₐ[R] Sh, IsLocalHom f' →
        f'.toRingHom.comp (algebraMap Rp Rh) = algebraMap Rp Sh → f' = f) ∧
      let g : Rh ⊗[R] S →ₐ[R] Sh :=
        Algebra.TensorProduct.lift f (IsScalarTower.toAlgHom R S Sh)
          (fun _ _ => Commute.all _ _)
      ∃ (Q : Ideal (Rh ⊗[R] S)) (_hQ : Q.IsPrime),
        Q.comap (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := Rh) (B := S)) =
            maximalIdeal Rh ∧
        Q.comap (Algebra.TensorProduct.includeRight (R := R) (A := Rh) (B := S)).toRingHom = q ∧
        Q = (maximalIdeal Sh).comap g.toRingHom ∧
        (∀ (Q' : Ideal (Rh ⊗[R] S)), Q'.IsPrime →
          Q'.comap (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := Rh) (B := S)) =
              maximalIdeal Rh →
          Q'.comap (Algebra.TensorProduct.includeRight (R := R) (A := Rh) (B := S)).toRingHom =
              q → Q' = Q) ∧
        ∃ alg : Algebra (Localization.AtPrime Q) Sh,
          letI : Algebra (Localization.AtPrime Q) Sh := alg
          ∃ _ : IsLocalHom (algebraMap (Localization.AtPrime Q) Sh),
            IsHenselization (Localization.AtPrime Q)
                (ResidueField (Localization.AtPrime Q)) Sh ∧
              (algebraMap (Localization.AtPrime Q) Sh).comp
                  (algebraMap (Rh ⊗[R] S) (Localization.AtPrime Q)) = g.toRingHom
```

## Tag 04GT, a lemma

[Tag 04GT](https://stacks.math.columbia.edu/tag/04GT) in the Stacks Project.

**`Stacks.StrictHenselization.strict_henselization_universal_property`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization.lean, line 1104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization.lean#L1104).

> **Theorem (Stacks Tag 04GT).** Let `φ : R → S` be a local ring map of local rings,
> let `κ(S) ⊂ κsep` be a separable algebraic closure of the residue field of `S`, and let
> `S → Ssh` be a strict henselization of `S` with respect to it. Let `R → A` be an étale
> ring map and `q` a prime of `A` lying over `m_R`. Given a residue field point
> `φbar : κ(q) → κsep` making the residue field square commute, there is a unique ring map
> `f : A → Ssh` compatible over the base, with `f⁻¹(m_{Ssh}) = q`, and inducing `φbar` on
> residue fields (via the identification `κ(Ssh) ≅ κsep`).

```lean
theorem strict_henselization_universal_property
    -- Local rings and the local base map `φ : R → S`.
    {R S : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    (φ : R →+* S) [IsLocalHom φ]
    -- A separable algebraic closure `κ(S) ⊂ κsep` of the residue field of `S` (Definition 2).
    (κsep : Type*) [Field κsep] [Algebra (maximalIdeal S).ResidueField κsep]
      [IsSepClosure (maximalIdeal S).ResidueField κsep]
    -- The strict henselization `S → Ssh` (Definition 3).
    {Ssh : Type*} [CommRing Ssh] [IsLocalRing Ssh] [Algebra S Ssh]
    (hsh : IsStrictHenselization S κsep Ssh)
    -- An étale `R`-algebra `A` and a prime `q` lying over `m_R`.
    {A : Type*} [CommRing A] [Algebra R A] [Algebra.Etale R A]
    (q : Ideal A) [q.IsPrime] (hq : maximalIdeal R = q.comap (algebraMap R A))
    -- The given residue field point `φbar : κ(q) → κsep`.
    (φbar : q.ResidueField →+* κsep)
    -- Compatibility of the residue square:
    --   `φbar ∘ (κ(R) → κ(q)) = (κ(S) → κsep) ∘ (κ(R) → κ(S))`.
    (hsquare :
      φbar.comp (Ideal.ResidueField.map (maximalIdeal R) q (algebraMap R A) hq)
        =
      (algebraMap (maximalIdeal S).ResidueField κsep).comp
        (Ideal.ResidueField.map (maximalIdeal R) (maximalIdeal S) φ
          (maximalIdeal_comap φ).symm)) :
    ∃! f : A →+* Ssh,
      -- (1) Compatibility over the base.
      (f.comp (algebraMap R A) = (algebraMap S Ssh).comp φ) ∧
      -- (2) Prime condition: `f⁻¹(m_{Ssh}) = q`.
      (∃ hf : q = (maximalIdeal Ssh).comap f,
        -- (3) Residue field condition: the induced `κ(q) → κ(Ssh)` equals
        --     `κ(q) --φbar--> κsep ≃ κ(Ssh)`.
        Ideal.ResidueField.map q (maximalIdeal Ssh) f hf
          = (hsh.residueFieldEquiv : κsep →+* (maximalIdeal Ssh).ResidueField).comp φbar)
```

## Tag 04GU, a lemma

[Tag 04GU](https://stacks.math.columbia.edu/tag/04GU) in the Stacks Project.

**`HenselianLocalRing.indEtaleAlgHomOfResidue`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization.lean#L392). The attribute's comment: “The map of the universal property: the target is an arbitrary henselian local `R`-algebra `Ssh`, since the source's `S` enters only through the composite `R → S → S^sh`, and of `R^sh` only locality and ind-étaleness — `(CommAlgCat.etale R).ind`, the spelling of Lemma 04GP(3) — are used. The source's square of residue fields is `hφ`, stated at the level of `R`; `R` local and both structure maps local are consequences of it, not hypotheses. `isLocalHom_indEtaleAlgHomOfResidue`, `comp_residue_indEtaleAlgHomOfResidue` and `indEtaleAlgHomOfResidue_unique` are its two properties and its uniqueness. See the module docstring.”. References: EGA IV (18.8.8.1), “existence of A^hs->B”; EGA IV (18.8.8).

> **The map given by functoriality of the strict henselization** (Stacks 04GU). Let `R` be a
> ring, let `Rsh` be a local `R`-algebra which is a filtered colimit of étale `R`-algebras, let
> `Ssh` be a henselian local `R`-algebra, and let `φ : ResidueField Rsh →+* ResidueField Ssh` be
> compatible with the residue maps of `R → Rsh` and `R → Ssh`. This is the `R`-algebra map
> `f : Rsh → Ssh` inducing `φ` on residue fields; it is a local ring map, and is the only such map.
> Applied to strict henselizations `Rsh = R^sh` and `Ssh = S^sh` of a local map of local rings
> `R → S`, and to a map `φ : κ₁^sep → κ₂^sep` of separable algebraic closures over the residue field
> map of `R → S`, it is the local ring map `R^sh → S^sh` over `R → S` inducing `φ`.

```lean
noncomputable def HenselianLocalRing.indEtaleAlgHomOfResidue
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rsh)))
    (φ : ResidueField Rsh →+* ResidueField Ssh)
    (hφ : φ.comp ((residue Rsh).comp (algebraMap R Rsh))
      = (residue Ssh).comp (algebraMap R Ssh)) :
    Rsh →ₐ[R] Ssh
```

**`HenselianLocalRing.comp_residue_indEtaleAlgHomOfResidue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization.lean#L405). The attribute's comment: “the defining property of `indEtaleAlgHomOfResidue`”. References: EGA IV (18.8.8.1), “induces \psi on residues”; EGA IV (18.8.4), “partial”.

> `HenselianLocalRing.indEtaleAlgHomOfResidue` induces `φ` on residue fields.

```lean
public theorem HenselianLocalRing.comp_residue_indEtaleAlgHomOfResidue
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rsh)))
    (φ : ResidueField Rsh →+* ResidueField Ssh)
    (hφ : φ.comp ((residue Rsh).comp (algebraMap R Rsh))
      = (residue Ssh).comp (algebraMap R Ssh)) :
    (residue Ssh).comp
        (HenselianLocalRing.indEtaleAlgHomOfResidue hind φ hφ : Rsh →+* Ssh)
      = φ.comp (residue Rsh)
```

**`HenselianLocalRing.isLocalHom_indEtaleAlgHomOfResidue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization.lean#L420). The attribute's comment: “`indEtaleAlgHomOfResidue` is local, which the source asserts”. References: EGA IV (18.8.8.1), “locality of A^hs->B”.

> `HenselianLocalRing.indEtaleAlgHomOfResidue` is a local ring map.

```lean
public theorem HenselianLocalRing.isLocalHom_indEtaleAlgHomOfResidue
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rsh)))
    (φ : ResidueField Rsh →+* ResidueField Ssh)
    (hφ : φ.comp ((residue Rsh).comp (algebraMap R Rsh))
      = (residue Ssh).comp (algebraMap R Ssh)) :
    IsLocalHom (HenselianLocalRing.indEtaleAlgHomOfResidue hind φ hφ)
```

**`HenselianLocalRing.indEtaleAlgHomOfResidue_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization.lean#L433). The attribute's comment: “uniqueness of `indEtaleAlgHomOfResidue`”. References: EGA IV (18.8.8.1), “uniqueness of A^hs->B”.

> `HenselianLocalRing.indEtaleAlgHomOfResidue` is the only local `R`-algebra map `Rsh → Ssh`
> inducing `φ` on residue fields.

```lean
public theorem HenselianLocalRing.indEtaleAlgHomOfResidue_unique
    (hind : (CommAlgCat.etale.{max u v} R).ind.{max u v}
      (CommAlgCat.of R (ULift.{u} Rsh)))
    (φ : ResidueField Rsh →+* ResidueField Ssh)
    (hφ : φ.comp ((residue Rsh).comp (algebraMap R Rsh))
      = (residue Ssh).comp (algebraMap R Ssh))
    (f : Rsh →ₐ[R] Ssh) (hfloc : IsLocalHom f)
    (hf : (residue Ssh).comp (f : Rsh →+* Ssh) = φ.comp (residue Rsh)) :
    f = HenselianLocalRing.indEtaleAlgHomOfResidue hind φ hφ
```

**`Stacks.StrictHenselization.IsStrictHenselization.existsUnique_algHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/StrictlyHenselianTarget.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/StrictlyHenselianTarget.lean#L167). The attribute's comment: “The universal property read off `IsStrictHenselization`: the residue datum is a map out of the chosen separable closure `κ^sep` rather than out of `IsLocalRing.ResidueField R`, the convention `HenselianLocalRing.indEtaleAlgHomOfResidue` is phrased in, and the target is an arbitrary henselian local `A`-algebra as there. Existence and uniqueness among local `A`-algebra maps are the source's two assertions.”. References: EGA IV (18.8.8), “more general”; EGA IV (18.8.9), “special case”; SGA 4 VIII (4.4), “more general”.

> **The universal property of the strict henselization against a henselian local algebra**
> (Stacks 04GU). Let `A` be a local ring, let `κ^sep` be a separable algebraic closure of its
> residue field and let `R` be a strict henselization of `A` with respect to it. Let `C` be a
> henselian local `A`-algebra, and let `χ : κ^sep → κ(C)` be a ring map compatible with the residue
> maps of `A → R` and `A → C` (the square of fields of the source). Then there is exactly one local
> `A`-algebra map `R → C` inducing `χ` on residue fields.
>
> The source states this for `C` a strict henselization of a local ring `S` receiving a local map
> from `A`; Lemma 04GU uses of `C` only that it is a henselian local `A`-algebra, and that is the
> form taken here, since the target that this is applied to is known to be strictly henselian before
> it is known to be a strict henselization.

```lean
theorem IsStrictHenselization.existsUnique_algHom (hR : IsStrictHenselization A κsep R)
    {C : Type*} [CommRing C] [HenselianLocalRing C] [Algebra A C]
    (χ : κsep →+* ResidueField C)
    (hχ : ∀ a : A, χ (algebraMap (maximalIdeal A).ResidueField κsep
        (algebraMap A (maximalIdeal A).ResidueField a))
      = residue C (algebraMap A C a)) :
    ∃! f : R →ₐ[A] C, IsLocalHom f ∧
      (residue C).comp (f : R →+* C) = (χ.comp hR.residueFieldHom).comp (residue R)
```

**`Stacks.StrictHenselization.IsStrictHenselization.exists_algHom_of_isSepClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/StrictlyHenselianTarget.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/StrictlyHenselianTarget.lean#L200). The attribute's comment: “The source's map, in the case where the target's residue field is only known to be separably closed rather than identified with a chosen separable closure: the residue datum is then not part of the input but produced by `IsSepClosed.lift`, and only existence survives.”. References: EGA IV (18.8.8), “(ii)”.

> **A strictly henselian local algebra receives a local map from the strict henselization.**
> Let `A` be a local ring, let `κ^sep` be a separable algebraic closure of its residue field and let
> `R` be a strict henselization of `A` with respect to it. Let `C` be a henselian local `A`-algebra
> with separably closed residue field whose structure map is local. Then there is a local
> `A`-algebra map `R → C`.
>
> No residue datum has to be supplied: `κ^sep` is separable over `κ_A` and `κ(C)` is a separably
> closed field over `κ_A` through the residue map of `A → C`, so `IsSepClosed.lift` produces one,
> and `existsUnique_algHom` turns it into the map. Uniqueness is *not* asserted, and genuinely
> fails: the local maps `R → C` over `A` are permuted by the automorphisms of `κ^sep` over `κ_A`,
> and it is the residue datum that singles one out.

```lean
theorem IsStrictHenselization.exists_algHom_of_isSepClosed (hR : IsStrictHenselization A κsep R)
    (C : Type*) [CommRing C] [HenselianLocalRing C] [Algebra A C]
    [IsLocalHom (algebraMap A C)] (hC : IsSepClosed (ResidueField C)) :
    ∃ f : R →ₐ[A] C, IsLocalHom f
```

## Tag 04GW, a lemma

[Tag 04GW](https://stacks.math.columbia.edu/tag/04GW) in the Stacks Project.

**`IsLocalRing.IsHenselization.isFiltered_augmentedEtale_and_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselizationColimit.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselizationColimit.lean#L324). The attribute's comment: “A triple `(S, q, φ)` is an étale `R`-algebra with an `R`-algebra map to `κ^sep`, whose kernel is `q`. The strict henselization of `R_p` with respect to `κ^sep` is `IsHenselization (Localization.AtPrime p) κsep Rsh`; the statement is proved for any extension `L` of `κ(p)`. `canonically` is the characterization of the colimit maps `S → Rsh`: given the identification `e : κ^sep ≅ κ(Rsh)`, they are the unique maps reducing to `S → κ^sep ≅ κ(Rsh)`; the maps `S_q → Rsh` extend them along `S → S_q`.”.

> **The strict henselization as a colimit of étale algebras** (Stacks 04GW). Let `p` be a prime
> of `R`, let `L` be an extension of `κ(p)` (a separable algebraic closure `κ^sep`, in the source),
> let `Rsh` be a henselization of `R_p` with residue field `L` (the strict henselization
> `(R_p)^{sh}`), and fix an isomorphism `e : L ≅ κ(Rsh)` compatible with the maps from `R`. The
> category of étale `R`-algebras `S` with an `R`-algebra map `S → L` — the triples `(S, q, φ)` — is
> filtered, and `Rsh` is canonically the colimit of the algebras `S` and also of the local rings
> `S_q`, where `q` is the kernel of `S → L`. The canonical maps `S → Rsh` are the unique `R`-algebra
> maps whose reduction is `S → L ≅ κ(Rsh)`, and the maps `S_q → Rsh` extend them.

```lean
theorem isFiltered_augmentedEtale_and_isColimit [IsScalarTower R (Localization.AtPrime p) Rsh] :
    IsFiltered (AugmentedEtale R L) ∧
      ∃ ι : forget R L ⟶ (Functor.const _).obj (CommAlgCat.of R Rsh),
        (∀ A x, residue Rsh ((ι.app A).hom x) = e (A.hom.hom x)) ∧
        (∀ ι' : forget R L ⟶ (Functor.const _).obj (CommAlgCat.of R Rsh),
          (∀ A x, residue Rsh ((ι'.app A).hom x) = e (A.hom.hom x)) → ι' = ι) ∧
        Nonempty (IsColimit (Cocone.mk _ ι)) ∧
        ∃ ιLoc : localization R L ⟶ (Functor.const _).obj (CommAlgCat.of R Rsh),
          (∀ A, (toLocalization R L).app A ≫ ιLoc.app A = ι.app A) ∧
          Nonempty (IsColimit (Cocone.mk _ ιLoc))
```

## Tag 08HV, a lemma

[Tag 08HV](https://stacks.math.columbia.edu/tag/08HV) in the Stacks Project.

**`IsLocalRing.IsHenselization.exists_prime_isStrictHenselization_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/TensorProduct.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/TensorProduct.lean#L70). The attribute's comment: “The separable algebraic closures are the residue fields of `R^sh` and `S^sh`, and the commutative square is the compatibility `hphi` of `φ` with the residue maps out of `R`. The map of 04GU is pinned as the unique local `R`-algebra map inducing `φ`. The prime is `g⁻¹(𝔪_{S^sh})` with its two contractions; that `S^sh` is the strict henselization of `(R^sh ⊗_R S)_Q` is `IsHenselization` with residue field `κ(S^sh)`, separably closed over `κ(Q)`. All rings share one universe, as `IsHenselization` requires.”.

> **The strict henselization after a ring map** (Stacks 08HV). Let `R → S` be a ring map and
> let `q ⊆ S` lie over `p ⊆ R`. Let `Rsh` and `Ssh` be strict henselizations of `R_p` and `S_q`,
> with respect to the separable algebraic closures `κ(Rsh)` of `κ(p)` and `κ(Ssh)` of `κ(q)`, and
> let `φ : κ(Rsh) → κ(Ssh)` be compatible with the residue maps out of `R`. The local map
> `f : Rsh → Ssh` of Lemma 04GU inducing `φ` identifies `Ssh` with the strict henselization of
> `Rsh ⊗[R] S` at the prime `Q = g⁻¹(𝔪_Ssh)`, where `g : Rsh ⊗[R] S → Ssh` is induced by `f`; `Q`
> lies over `𝔪_Rsh` and over `q`.

```lean
theorem exists_prime_isStrictHenselization_tensorProduct [Algebra R Sq] [Algebra Rp Sq]
    [IsScalarTower R S Sq] [IsScalarTower R Rp Sq] [Algebra Rp Ssh] [IsScalarTower R Rp Ssh]
    [IsScalarTower Rp Sq Ssh] (phi : ResidueField Rsh →+* ResidueField Ssh)
    (hphi : phi.comp ((residue Rsh).comp (algebraMap R Rsh)) =
      (residue Ssh).comp (algebraMap R Ssh)) :
    ∃ f : Rsh →ₐ[R] Ssh, IsLocalHom f ∧
      (residue Ssh).comp f.toRingHom = phi.comp (residue Rsh) ∧
      (∀ f' : Rsh →ₐ[R] Ssh, IsLocalHom f' →
        (residue Ssh).comp f'.toRingHom = phi.comp (residue Rsh) → f' = f) ∧
      let g : Rsh ⊗[R] S →ₐ[R] Ssh :=
        Algebra.TensorProduct.lift f (IsScalarTower.toAlgHom R S Ssh) fun _ _ => .all _ _
      ∃ (Q : Ideal (Rsh ⊗[R] S)) (_ : Q.IsPrime),
        Q.comap (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := Rsh) (B := S)) =
          maximalIdeal Rsh ∧
        Q.comap (Algebra.TensorProduct.includeRight (R := R) (A := Rsh) (B := S)).toRingHom = q ∧
        Q = (maximalIdeal Ssh).comap g.toRingHom ∧
        ∃ _ : Algebra (Localization.AtPrime Q) Ssh,
          IsLocalHom (algebraMap (Localization.AtPrime Q) Ssh) ∧
          ∃ _ : Algebra (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh),
            IsSepClosure (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh) ∧
            IsHenselization (Localization.AtPrime Q) (ResidueField Ssh) Ssh ∧
            (∀ x, algebraMap (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh)
              (residue (Localization.AtPrime Q) x) =
                residue Ssh (algebraMap (Localization.AtPrime Q) Ssh x)) ∧
            (algebraMap (Localization.AtPrime Q) Ssh).comp
              (algebraMap (Rsh ⊗[R] S) (Localization.AtPrime Q)) = g.toRingHom
```

**`StacksDraft.strictHenselization_tensorProduct_at_induced_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HenselizationUniverse/StrictTensorProduct.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HenselizationUniverse/StrictTensorProduct.lean#L76). The attribute's comment: “Stated over six independent universes, as the source requires: the tag's six rings `R`, `R_p`, `R^sh`, `S`, `S_q`, `S^sh` are unconstrained relative to one another.”.

> **Strict henselization after a ring map** (Stacks 08HV), at six independent universes. For
> primes `q` over `p` and compatible separable closures of their residue fields, the canonical local
> map between strict henselizations identifies the target with the strict henselization of
> `Rsh ⊗[R] S` at the prime induced by that map.
>
> This is the source-strength form of tag 08HV, and the provider of that tag. The weaker
> single-universe statement
> `IsLocalRing.IsHenselization.exists_prime_isStrictHenselization_tensorProduct` pins all six rings
> to one `Type u`; its `@[stacks 08HV]` attribute is dropped in favour of this one. See the module
> docstring.

```lean
theorem strictHenselization_tensorProduct_at_induced_prime
    {R : Type uR} {Rp : Type uRp} {Rsh : Type uRsh}
    {S : Type uS} {Sq : Type uSq} {Ssh : Type uSsh}
    [CommRing R] [CommRing S] [Algebra R S]
    (p : Ideal R) (q : Ideal S) [p.IsPrime] [q.IsPrime] [q.LiesOver p]
    [CommRing Rp] [IsLocalRing Rp] [Algebra R Rp] [IsLocalization.AtPrime Rp p]
    [CommRing Sq] [IsLocalRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq q]
    [Algebra R Sq] [Algebra Rp Sq] [IsScalarTower R S Sq] [IsScalarTower R Rp Sq]
    [CommRing Rsh] [IsLocalRing Rsh] [Algebra R Rsh] [Algebra Rp Rsh]
    [IsScalarTower R Rp Rsh]
    [Algebra (ResidueField Rp) (ResidueField Rsh)]
    [IsSepClosure (ResidueField Rp) (ResidueField Rsh)]
    [IsHenselization Rp (ResidueField Rsh) Rsh]
    [CommRing Ssh] [IsLocalRing Ssh] [Algebra R Ssh] [Algebra S Ssh] [Algebra Rp Ssh]
    [Algebra Sq Ssh] [IsScalarTower R S Ssh] [IsScalarTower S Sq Ssh]
    [IsScalarTower R Rp Ssh] [IsScalarTower Rp Sq Ssh]
    [Algebra (ResidueField Sq) (ResidueField Ssh)]
    [IsSepClosure (ResidueField Sq) (ResidueField Ssh)]
    [IsHenselization Sq (ResidueField Ssh) Ssh]
    (phi : ResidueField Rsh →+* ResidueField Ssh)
    (hphi : phi.comp ((residue Rsh).comp (algebraMap R Rsh)) =
      (residue Ssh).comp (algebraMap R Ssh)) :
    ∃ f : Rsh →ₐ[R] Ssh,
      IsLocalHom f ∧
      (residue Ssh).comp f.toRingHom = phi.comp (residue Rsh) ∧
      (∀ f' : Rsh →ₐ[R] Ssh, IsLocalHom f' →
        (residue Ssh).comp f'.toRingHom = phi.comp (residue Rsh) → f' = f) ∧
      let g : Rsh ⊗[R] S →ₐ[R] Ssh :=
        Algebra.TensorProduct.lift f (IsScalarTower.toAlgHom R S Ssh)
          (fun _ _ => Commute.all _ _)
      ∃ (Q : Ideal (Rsh ⊗[R] S)) (_hQ : Q.IsPrime),
        Q.comap (Algebra.TensorProduct.includeLeftRingHom (R := R) (A := Rsh) (B := S)) =
            maximalIdeal Rsh ∧
        Q.comap (Algebra.TensorProduct.includeRight (R := R) (A := Rsh) (B := S)).toRingHom = q ∧
        Q = (maximalIdeal Ssh).comap g.toRingHom ∧
        ∃ alg : Algebra (Localization.AtPrime Q) Ssh,
          letI : Algebra (Localization.AtPrime Q) Ssh := alg
          ∃ _ : IsLocalHom (algebraMap (Localization.AtPrime Q) Ssh),
            ∃ algRes : Algebra (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh),
              letI : Algebra (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh) := algRes
              IsSepClosure (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh) ∧
                IsHenselization (Localization.AtPrime Q) (ResidueField Ssh) Ssh ∧
                (∀ x : Localization.AtPrime Q,
                  algebraMap (ResidueField (Localization.AtPrime Q)) (ResidueField Ssh)
                      (residue (Localization.AtPrime Q) x) =
                    residue Ssh (algebraMap (Localization.AtPrime Q) Ssh x)) ∧
                (algebraMap (Localization.AtPrime Q) Ssh).comp
                    (algebraMap (Rsh ⊗[R] S) (Localization.AtPrime Q)) = g.toRingHom
```

## Tag 0C2Z, a lemma

[Tag 0C2Z](https://stacks.math.columbia.edu/tag/0C2Z) in the Stacks Project.

**`IsLocalRing.IsHenselization.exists_algEquiv_tensorProduct_strictHenselization_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Henselian/StrictHenselization/BaseChange.lean, line 689](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Henselian/StrictHenselization/BaseChange.lean#L689). The attribute's comment: “The equality of the source is an isomorphism of `(S_q)^h`-algebras `Ssh ≃ₐ[Sh] Sh ⊗[Rh] Rsh` compatible with the local map `Rsh → Ssh` over `Rh` inducing the identity of `κ^sep` (via `eRsh`, `eSsh`), which is part of the statement. Henselizations and strict henselizations are `IsHenselization` with residue field `κ` and `κ^sep`. All seven carriers — `R`, `S`, `κ^sep`, `(R_p)^h`, `(S_q)^h`, `(R_p)^{sh}`, `(S_q)^{sh}` — lie in mutually independent universes.”.

> **The strict henselization as a base change of the henselization** (Stacks 0C2Z). Let
> `R → S` be a ring map and let `q` be a prime of `S` lying over the prime `p` of `R` such that
> `κ(p) → κ(q)` is an isomorphism, and let `κ^sep` be a separable algebraic closure of
> `κ(p) = κ(q)`. Let `(R_p)^h → (S_q)^h` be henselizations over `R_p → S_q` and let `(R_p)^{sh}`,
> `(S_q)^{sh}` be strict henselizations with respect to `κ^sep`. Then the local map
> `(R_p)^{sh} → (S_q)^{sh}` over `(R_p)^h` inducing the identity of `κ^sep` identifies
> `(S_q)^{sh}` with `(S_q)^h ⊗_{(R_p)^h} (R_p)^{sh}`.

```lean
theorem IsLocalRing.IsHenselization.exists_algEquiv_tensorProduct_strictHenselization_atPrime
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S] (p : Ideal R) (q : Ideal S)
    [p.IsPrime] [q.IsPrime] [q.LiesOver p]
    [Algebra (Localization.AtPrime p) (Localization.AtPrime q)]
    [Localization.AtPrime.IsLiesOverAlgebra p q]
    (hres : Function.Bijective
      (ResidueField.map (algebraMap (Localization.AtPrime p) (Localization.AtPrime q))))
    (ksep : Type w) [Field ksep] [Algebra (ResidueField (Localization.AtPrime p)) ksep]
    [Algebra (ResidueField (Localization.AtPrime q)) ksep]
    [IsSepClosure (ResidueField (Localization.AtPrime p)) ksep]
    [IsSepClosure (ResidueField (Localization.AtPrime q)) ksep]
    (hksep : ∀ a, algebraMap (ResidueField (Localization.AtPrime q)) ksep
      (ResidueField.map (algebraMap (Localization.AtPrime p) (Localization.AtPrime q)) a) =
        algebraMap (ResidueField (Localization.AtPrime p)) ksep a)
    (Rh : Type x) [CommRing Rh] [IsLocalRing Rh] [Algebra (Localization.AtPrime p) Rh]
    [IsHenselization (Localization.AtPrime p) (ResidueField (Localization.AtPrime p)) Rh]
    (Sh : Type y) [CommRing Sh] [IsLocalRing Sh] [Algebra (Localization.AtPrime q) Sh]
    [IsHenselization (Localization.AtPrime q) (ResidueField (Localization.AtPrime q)) Sh]
    [Algebra (Localization.AtPrime p) Sh] [Algebra Rh Sh]
    [IsScalarTower (Localization.AtPrime p) Rh Sh]
    [IsScalarTower (Localization.AtPrime p) (Localization.AtPrime q) Sh]
    [IsLocalHom (algebraMap Rh Sh)]
    (Rsh : Type z) [CommRing Rsh] [IsLocalRing Rsh] [Algebra (Localization.AtPrime p) Rsh]
    [Algebra Rh Rsh] [IsScalarTower (Localization.AtPrime p) Rh Rsh]
    [IsHenselization (Localization.AtPrime p) ksep Rsh]
    (Ssh : Type t) [CommRing Ssh] [IsLocalRing Ssh] [Algebra (Localization.AtPrime q) Ssh]
    [Algebra Sh Ssh] [Algebra (Localization.AtPrime p) Ssh] [Algebra Rh Ssh]
    [IsScalarTower (Localization.AtPrime q) Sh Ssh]
    [IsScalarTower (Localization.AtPrime p) (Localization.AtPrime q) Ssh]
    [IsScalarTower (Localization.AtPrime p) Rh Ssh] [IsScalarTower Rh Sh Ssh]
    [IsHenselization (Localization.AtPrime q) ksep Ssh]
    (eRsh : ksep ≃+* ResidueField Rsh)
    (heRsh : ∀ a, eRsh (algebraMap (ResidueField (Localization.AtPrime p)) ksep
      (residue (Localization.AtPrime p) a)) =
        residue Rsh (algebraMap (Localization.AtPrime p) Rsh a))
    (eSsh : ksep ≃+* ResidueField Ssh)
    (heSsh : ∀ b, eSsh (algebraMap (ResidueField (Localization.AtPrime q)) ksep
      (residue (Localization.AtPrime q) b)) =
        residue Ssh (algebraMap (Localization.AtPrime q) Ssh b)) :
    ∃ g : Rsh →ₐ[Rh] Ssh, IsLocalHom g ∧
      (∀ a, eSsh.symm (residue Ssh (g a)) = eRsh.symm (residue Rsh a)) ∧
      ∃ e : Ssh ≃ₐ[Sh] Sh ⊗[Rh] Rsh, ∀ a, e (g a) = Algebra.TensorProduct.includeRight a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.155, Tag 0BSK](https://stacks.math.columbia.edu/tag/0BSK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
