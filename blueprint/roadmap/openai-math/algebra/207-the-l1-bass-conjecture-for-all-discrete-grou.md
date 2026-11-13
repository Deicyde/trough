---
declaration: section
origin: cited
lean: OAI.BassTrace.RightProjective.bassTraceModules_vanishing_and_support, OAI.TorsionFreeBass.torsion_free_corollary
statement: formalized
proof: formalized
---

# 207. The ℓ¹-Bass conjecture for all discrete groups

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves the $ℓ^{1}$-Bass conjecture for every discrete group: Hattori–Stallings traces of idempotent matrices over $\ell^1(G)$ are supported on finitely many finite-order conjugacy classes. The algebraic companion proves the integral Bass trace conjecture and Kaplansky's idempotent conjecture for torsion-free groups over every commutative unital characteristic-zero domain.

## The ℓ¹-Bass Conjecture for Discrete Groups

We prove the $ℓ^{1}$-Bass conjecture for every discrete group. The Hattori–Stallings trace of every idempotent matrix over the complex $ℓ^{1}$ group algebra is supported on finitely many conjugacy classes of finite-order elements.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-l1-Bass-Conjecture-for-Discrete-Groups-October-5-2026/l1-bass-conjecture.pdf).

## The Bass trace conjecture and the characteristic-zero Kaplansky idempotent conjecture

We prove the complex group-ring Bass trace conjecture for every discrete group: the Hattori–Stallings trace of a finitely generated projective module over its complex group ring is supported on conjugacy classes of finite-order elements. As a consequence, for every torsion-free group *G* and every commutative unital domain *R* of characteristic zero, the only idempotents in $RG$ are 0 and 1. This proves Kaplansky's idempotent conjecture in characteristic zero.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the complex Bass trace conjecture for every group: the Hattori–Stallings trace of each virtual class of finitely generated projective right $\mathbb C[G]$-modules vanishes on conjugacy classes of infinite-order elements. No finiteness, countability, or geometric hypothesis on $G$ is imposed.

For torsion-free $G$, it identifies the trace on $K_0(\mathbb C[G])$ with the integral augmentation rank and proves the characteristic-zero Kaplansky idempotent conjecture: for every commutative unital domain $R$ of characteristic zero, an idempotent in $R[G]$ is $0$ or $1$.

## Lean: Complex Bass trace vanishing and support

```lean
theorem bassTraceModules_vanishing_and_support {G : Type u} [_root_.Group G]
    (x : ModuleK0.{u,v} (MonoidAlgebra ℂ G)) :
    (∀ g : G, ¬IsOfFinOrder g → HattoriStallings x (ConjClasses.mk g) = 0) ∧
      ↑(HattoriStallings x).support ⊆
        {c | ∃ g : G, IsOfFinOrder g ∧ ConjClasses.mk g = c}
```

Stated in [BassTrace.lean, line 470](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BassTrace.lean#L470). Proved in [lean/OAI/RingTheory/BassTrace/Main.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RingTheory/BassTrace/Main.lean#L23). formalization.yaml lists it as one of the repository's main results.

## Lean: Trace rank and characteristic-zero Kaplansky idempotents for torsion-free groups

```lean
theorem torsion_free_corollary (G : Type*) [Group G] (hG : TorsionFree G) :
    ((∀ (q : ℕ), 1 ≤ q →
      ∀ e : Matrix (Fin q) (Fin q) (MonoidAlgebra ℂ G), e ^ 2 = e →
        matrixTrace e = ((augmentedMatrix e).rank : ℂ)) ∧
      traceK0 (G := G) = (Int.castAddHom ℂ).comp augmentationRank ∧
      Set.range (traceK0 (G := G)) = Set.range (fun z : ℤ => (z : ℂ))) ∧
    (∀ (R : Type*) [CommRing R] [IsDomain R] [CharZero R]
      (e : MonoidAlgebra R G), e ^ 2 = e → e = 0 ∨ e = 1)
```

Stated in [BassTorsionFree.lean, line 299](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BassTorsionFree.lean#L299). Proved in [lean/OAI/RingTheory/BassTrace/TorsionFree.lean, line 50](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RingTheory/BassTrace/TorsionFree.lean#L50).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/207.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/207.md)
