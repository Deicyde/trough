---
declaration: section
origin: cited
lean: Module.Flat.baseChange_and_of_flat_baseChange_of_isPushout_of_isLocalization, Module.Flat.baseChange_of_map_maximalIdeal_eq_maximalIdeal
statement: formalized
proof: formalized
---

# 10.100 Base change and flatness

Section 10.100 of the Stacks Project, [Tag 051D](https://stacks.math.columbia.edu/tag/051D). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00MQ, a lemma

[Tag 00MQ](https://stacks.math.columbia.edu/tag/00MQ) in the Stacks Project.

**`Module.Flat.baseChange_and_of_flat_baseChange_of_isPushout_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BaseChange.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/BaseChange.lean#L267). The attribute's comment: “Parts (1) and (2). Of the source's eight locality assumptions only `IsLocalRing S`, `IsLocalRing S'` and `IsLocalHom (algebraMap S S')` are used, by part (2) alone, and they are bound inside the second conjunct together with `Module.Flat R R'`, so that part (1) is stated for an arbitrary commutative square; the rest are dropped. "`S'` is a localization of `S ⊗_R R'`" is `IsLocalization W S'` over an abstract pushout `Algebra.IsPushout R S R' T`, as in the siblings 00P4 and 00RJ, and `M' = S' ⊗_S M` is `IsBaseChange S' f`, as in 00MO. Parts (3) and (4) are the instance `M := S`, `M' := S'` and are not separate declarations. See the module docstring.”.

> **Stacks 00MQ**, parts (1) and (2). Let `S ← R → R'` be ring maps, let `T` be the pushout
> `S ⊗_R R'`, let `S'` be a localization of `T` at a submonoid `W`, and let `f : M →ₗ[S] M'` realize
> `M'` as the base change `S' ⊗_S M` of an `S`-module `M`. Then (1) if `M` is flat over `R` then
> `M'` is flat over `R'`, and (2) if moreover `S` and `S'` are local with `S → S'` a local
> homomorphism, then `M'` flat over `R'` and `R → R'` flat imply `M` flat over `R`.
>
> Part (1) holds for an arbitrary such square: the source's local rings and local homomorphisms are
> used only in part (2), and only for `S`, `S'` and `S → S'`, so they are bound inside the second
> conjunct instead of in the signature.
>
> Parts (3) and (4) of the source, that `S` flat over `R` implies `S'` flat over `R'` and that
> `R' → S'` and `R → R'` flat imply `S` flat over `R`, are the instance `M := S`, `M' := S'`,
> `f := Algebra.linearMap S S'`; see the module docstring.

```lean
public theorem baseChange_and_of_flat_baseChange_of_isPushout_of_isLocalization
    (R : Type*) {S R' T S' M M' : Type*}
    [CommRing R] [CommRing S] [CommRing R'] [CommRing T] [CommRing S']
    [Algebra R S] [Algebra R R'] [Algebra R T] [Algebra S T] [Algebra R' T]
    [IsScalarTower R S T] [IsScalarTower R R' T] [Algebra.IsPushout R S R' T]
    [Algebra S S'] [Algebra R' S'] [Algebra T S']
    [IsScalarTower S T S'] [IsScalarTower R' T S']
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [AddCommGroup M'] [Module S M'] [Module R' M'] [Module S' M']
    [IsScalarTower S S' M'] [IsScalarTower R' S' M']
    (W : Submonoid T) [IsLocalization W S'] (f : M →ₗ[S] M') (hf : IsBaseChange S' f) :
    (Module.Flat R M → Module.Flat R' M') ∧
      (∀ [IsLocalRing S] [IsLocalRing S'] [IsLocalHom (algebraMap S S')],
        Module.Flat R' M' → Module.Flat R R' → Module.Flat R M)
```

## Tag 0GEB, a lemma

[Tag 0GEB](https://stacks.math.columbia.edu/tag/0GEB) in the Stacks Project.

**`Module.Flat.baseChange_of_map_maximalIdeal_eq_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalBaseChange.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/LocalBaseChange.lean#L254). The attribute's comment: “The commutative square is presented by the two scalar towers into `S'`, `M ⊗_S S'` by `IsBaseChange S' f` as in the sibling 00MO, and `𝔪_R R'` by `Ideal.map (algebraMap R R') (IsLocalRing.maximalIdeal R)`. The source's unused hypotheses `S` local, `R → S` local and `S → S'` local are dropped, and `R → R'` local is implied by `hm`. See the module docstring.”.

> **Stacks 0GEB.** Let `S ← R → R'`, `S → S'`, `R' → S'` be a commutative diagram of local
> rings and local homomorphisms, let `M` be a finite `S`-module and let `f : M → M'` realize `M'` as
> the base change `M ⊗_S S'`. Assume the horizontal arrows `R → R'` and `S → S'` are flat, that `M`
> is flat over `R`, that `𝔪_R R' = 𝔪_{R'}` and that `R'` and `S'` are Noetherian. Then `M'` is flat
> over `R'`.

```lean
public theorem baseChange_of_map_maximalIdeal_eq_maximalIdeal
    {R S R' S' M M' : Type*} [CommRing R] [CommRing S] [CommRing R'] [CommRing S']
    [IsLocalRing R] [IsLocalRing R'] [IsLocalRing S']
    [IsNoetherianRing R'] [IsNoetherianRing S']
    [Algebra R S] [Algebra R R'] [Algebra S S'] [Algebra R' S'] [Algebra R S']
    [IsScalarTower R S S'] [IsScalarTower R R' S']
    [IsLocalHom (algebraMap R' S')]
    [Module.Flat R R'] [Module.Flat S S']
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.Finite S M] [Module.Flat R M]
    [AddCommGroup M'] [Module S M'] [Module R' M'] [Module S' M']
    [IsScalarTower S S' M'] [IsScalarTower R' S' M']
    (hm : (IsLocalRing.maximalIdeal R).map (algebraMap R R') = IsLocalRing.maximalIdeal R')
    (f : M →ₗ[S] M') (hf : IsBaseChange S' f) :
    Module.Flat R' M'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.100, Tag 051D](https://stacks.math.columbia.edu/tag/051D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
