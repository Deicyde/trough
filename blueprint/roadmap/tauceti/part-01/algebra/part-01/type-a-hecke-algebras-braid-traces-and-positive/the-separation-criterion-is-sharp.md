---
declaration: theorem
origin: cited
lean: YoungDiagram.injOn_zpow_cellContent_iff
statement: formalized
proof: formalized
---

# The separation criterion is sharp

The powers `Q ^ content c` separate the addable cells
of every Young diagram of size less than `n` if and only if `Q ^ d ≠ 1` for `2 ≤ d ≤ n`.

```lean
YoungDiagram.injOn_zpow_cellContent_iff.{u_1} {G : Type u_1} [Group G] {Q : G} {n : ℕ} :
  (∀ (μ : YoungDiagram),
      μ.card < n → Set.InjOn (fun c => Q ^ YoungDiagram.cellContent c) {c | μ.IsAddable c}) ↔
    ∀ (d : ℕ), 2 ≤ d → d ≤ n → Q ^ d ≠ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`YoungDiagram.injOn_zpow_cellContent_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/Addable.html#YoungDiagram.injOn_zpow_cellContent_iff).

## Sources

- [Tau Ceti documentation: `YoungDiagram.injOn_zpow_cellContent_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Young/Addable.html#YoungDiagram.injOn_zpow_cellContent_iff)
- [Source of `YoungDiagram.injOn_zpow_cellContent_iff` in TauCeti/Combinatorics/Young/Addable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Young/Addable.lean#L383)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
