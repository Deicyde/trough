---
declaration: section
origin: cited
lean: MittagLeffler.IsMittagLefflerSet, MittagLeffler.IsMittagLefflerModule, DirInvSystem.nonempty_limit_of_isMittagLeffler, invLimit_exact
statement: formalized
proof: formalized
---

# 10.86 Mittag-Leffler systems

Section 10.86 of the Stacks Project, [Tag 0594](https://stacks.math.columbia.edu/tag/0594). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0595, a definition

[Tag 0595](https://stacks.math.columbia.edu/tag/0595) in the Stacks Project.

**`MittagLeffler.IsMittagLefflerSet`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean#L71). References: EGA 0 (13.1.2), “inverse systems of sets”; EGA 0 (13.1.3); EGA III (4.1.7); SGA 4½ Rapport (4.11).

> A directed inverse system of sets `(F_i, φ_{ji})` is *Mittag-Leffler*
> if for every index `i`, there exists some `j ≥ i` such that for all
> `k ≥ j`, the image of `F_k` in `F_i` (via the transition map) equals
> the image of `F_j` in `F_i`.

```lean
def IsMittagLefflerSet {ι : Type*} [Preorder ι] [IsDirected ι (· ≤ ·)] {F : ι → Type*}
    (φ : ⦃i j : ι⦄ → i ≤ j → F j → F i) [InverseSystem φ] : Prop
```

**`MittagLeffler.IsMittagLefflerModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean#L81). References: EGA 0 (13.1.2), “modules over a ring”; EGA III (4.1.7); SGA 4½ Rapport (4.11).

> A directed inverse system of `R`-modules `(M_i, φ_{ji})` is
> *Mittag-Leffler* if the underlying directed inverse system of sets is
> Mittag-Leffler.

```lean
def IsMittagLefflerModule {R : Type*} [Ring R] {ι : Type*} [Preorder ι]
    [IsDirected ι (· ≤ ·)] {M : ι → Type*} [∀ i, AddCommGroup (M i)] [∀ i, Module R (M i)]
    (φ : ⦃i j : ι⦄ → i ≤ j → M j →ₗ[R] M i)
    [InverseSystem (fun _ _ h => (φ h : M _ → M _))] : Prop
```

## Tag 0597, a lemma

[Tag 0597](https://stacks.math.columbia.edu/tag/0597) in the Stacks Project.

**`DirInvSystem.nonempty_limit_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean#L289). References: SGA 4 I (App.Lemma3), “more general”.

> Let `(A_i, φ_{ji})` be a directed inverse system of sets over a directed set `I`.
> If `I` is countable, the system is Mittag-Leffler, and each `A_i` is nonempty,
> then the limit `lim A_i` is nonempty.

```lean
theorem DirInvSystem.nonempty_limit_of_isMittagLeffler
    [Countable I] [Nonempty I] [IsDirected I (· ≤ ·)]
    {A : I → Type*} (S : DirInvSystem A)
    (hML : S.IsMittagLeffler) (hne : ∀ i, Nonempty (A i)) :
    S.limit.Nonempty
```

## Tag 0598, a lemma

[Tag 0598](https://stacks.math.columbia.edu/tag/0598) in the Stacks Project.

**`invLimit_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/MittagLeffler/InverseSystem.lean#L721). References: EGA 0 (13.2.2); EGA III (4.1.7.21), “more general”.

> Let `I` be a countable directed set and let
> `0 → A →[f] B →[g] C → 0` be an exact sequence of directed inverse systems of abelian
> groups over `I`.  If the system `(A, φ)` is Mittag-Leffler, then the induced sequence of
> inverse limits
> `0 → lim A →[lim f] lim B →[lim g] lim C → 0`
> is exact:
>
> 1. `lim f` is injective;
> 2. `range (lim f) = ker (lim g)`;
> 3. `lim g` is surjective.
>
> Left-exactness (parts 1 and 2) holds for any exact sequence of inverse systems; the
> Mittag-Leffler hypothesis and countability are used for part 3, the surjectivity of
> `lim g`.

```lean
theorem invLimit_exact
    {I : Type*} [Preorder I] [IsDirected I (· ≤ ·)] [Nonempty I] [Countable I]
    {A : I → Type*} [∀ i, AddCommGroup (A i)]
    {φ : ⦃i j : I⦄ → i ≤ j → (A j →+ A i)}
    (hφ : InverseSystem (fun _ _ h => (φ h : _ → _)))
    {B : I → Type*} [∀ i, AddCommGroup (B i)]
    {ψ : ⦃i j : I⦄ → i ≤ j → (B j →+ B i)}
    (hψ : InverseSystem (fun _ _ h => (ψ h : _ → _)))
    {C : I → Type*} [∀ i, AddCommGroup (C i)]
    {χ : ⦃i j : I⦄ → i ≤ j → (C j →+ C i)}
    (hχ : InverseSystem (fun _ _ h => (χ h : _ → _)))
    {f : ⦃i : I⦄ → (A i →+ B i)} {g : ⦃i : I⦄ → (B i →+ C i)}
    (hexact : IsExactSeq (φ := φ) (ψ := ψ) (χ := χ) f g)
    (hML : IsMittagLefflerSystem A φ) :
    Function.Injective (addInvLimit.map A φ B ψ f hexact.hf_mor) ∧
      (addInvLimit.map A φ B ψ f hexact.hf_mor).range =
        (addInvLimit.map B ψ C χ g hexact.hg_mor).ker ∧
      Function.Surjective (addInvLimit.map B ψ C χ g hexact.hg_mor)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.86, Tag 0594](https://stacks.math.columbia.edu/tag/0594)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
