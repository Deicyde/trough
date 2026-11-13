---
declaration: section
origin: cited
lean: InfinitesimalLifting.IsSmallExtension, Algebra.isSmoothAt_tfae
statement: formalized
proof: formalized
---

# 10.141 Smooth ring maps in the Noetherian case

Section 10.141 of the Stacks Project, [Tag 02HR](https://stacks.math.columbia.edu/tag/02HR). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02HS, a definition

[Tag 02HS](https://stacks.math.columbia.edu/tag/02HS) in the Stacks Project.

**`InfinitesimalLifting.IsSmallExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/InfinitesimalLifting.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/InfinitesimalLifting.lean#L129). References: SGA 7 VI (1.4), “more general”.

> A ring map `φ : B' → B` is a *small extension* (Stacks tag 02HS) if `B'` and
> `B` are local Artinian rings, `φ` is surjective, and the kernel `ker φ` has
> length `1` as a `B'`-module.

```lean
def IsSmallExtension {B' B : CommRingCat.{u}} (φ : B' ⟶ B) : Prop
```

## Tag 02HT, a lemma

[Tag 02HT](https://stacks.math.columbia.edu/tag/02HT) in the Stacks Project.

**`Algebra.isSmoothAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Kaehler/SmoothRingMapsInTheNoetherianCase.lean, line 479](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Kaehler/SmoothRingMapsInTheNoetherianCase.lean#L479). The attribute's comment: “Smoothness at `q` is `Algebra.IsSmoothAt`, the source's Definition 02HN by the finite presentation of `S`. A small extension (Definition 02HS) is a surjection `f : B' →ₐ[R] B` of Artinian local rings with `IsSimpleModule B' (ker f)`, and `κ(q) ≅ κ(𝔪)` is surjectivity of `Ideal.ResidueField.mapₐ q (maximalIdeal B) g`, the canonical map out of the residue field of `S_q` — not of `S → κ(𝔪)`, which would force `q` maximal. The source's prime `𝔭` under `q` is not used. See the module docstring.”.

> Let `R` be a Noetherian ring, let `S` be an `R`-algebra of finite type and let `q` be a prime
> of `S`. The following are equivalent:
>
> 1. `R → S` is smooth at `q`;
> 2. for every surjection `f : B' → B` of local `R`-algebras whose kernel has square zero and every
>    `R`-algebra map `g : S → B` with `q` the contraction of the maximal ideal of `B`, there is an
>    `R`-algebra map `g' : S → B'` with `f ∘ g' = g`;
> 3. the same, with `f` ranging over small extensions, that is, surjections of Artinian local rings
>    whose kernel is a simple `B'`-module (equivalently, has length `1`);
> 4. the same, with `f` ranging over small extensions along which `g` additionally induces an
>    isomorphism `κ(q) ≅ κ(𝔪)`, that is, along which the canonical map `κ(q) → κ(𝔪)` attached to
>    `q = g⁻¹(𝔪)` is surjective.

```lean
theorem isSmoothAt_tfae {R : Type u} {S : Type v} [CommRing R] [IsNoetherianRing R]
    [CommRing S] [Algebra R S] [Algebra.FiniteType R S] (q : Ideal S) [q.IsPrime] :
    List.TFAE
      [ Algebra.IsSmoothAt R q,
        ∀ (B' B : Type max u v) [CommRing B'] [CommRing B] [IsLocalRing B'] [IsLocalRing B]
          [Algebra R B'] [Algebra R B] (f : B' →ₐ[R] B), Function.Surjective f →
          RingHom.ker (f : B' →+* B) ^ 2 = ⊥ →
          ∀ g : S →ₐ[R] B, (maximalIdeal B).comap (g : S →+* B) = q →
            ∃ g' : S →ₐ[R] B', f.comp g' = g,
        ∀ (B' B : Type max u v) [CommRing B'] [CommRing B] [IsLocalRing B'] [IsLocalRing B]
          [IsArtinianRing B'] [IsArtinianRing B] [Algebra R B'] [Algebra R B]
          (f : B' →ₐ[R] B), Function.Surjective f →
          IsSimpleModule B' (RingHom.ker (f : B' →+* B)) →
          ∀ g : S →ₐ[R] B, (maximalIdeal B).comap (g : S →+* B) = q →
            ∃ g' : S →ₐ[R] B', f.comp g' = g,
        ∀ (B' B : Type max u v) [CommRing B'] [CommRing B] [IsLocalRing B'] [IsLocalRing B]
          [IsArtinianRing B'] [IsArtinianRing B] [Algebra R B'] [Algebra R B]
          (f : B' →ₐ[R] B), Function.Surjective f →
          IsSimpleModule B' (RingHom.ker (f : B' →+* B)) →
          ∀ (g : S →ₐ[R] B) (hq : (maximalIdeal B).comap (g : S →+* B) = q),
            Function.Surjective (Ideal.ResidueField.mapₐ q (maximalIdeal B) g hq.symm) →
            ∃ g' : S →ₐ[R] B', f.comp g' = g ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.141, Tag 02HR](https://stacks.math.columbia.edu/tag/02HR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
