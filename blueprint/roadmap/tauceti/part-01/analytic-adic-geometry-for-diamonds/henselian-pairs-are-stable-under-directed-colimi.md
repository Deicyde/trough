---
declaration: theorem
origin: cited
lean: Ring.DirectLimit.henselianRing
statement: formalized
proof: formalized
---

# Henselian pairs are stable under directed colimits

If every `(G i, I i)` is a
Henselian pair and the transition maps carry `I i` into `I j`, then the directed colimit
`Ring.DirectLimit G f` is Henselian along the colimit ideal `⨆ i, (I i).map (of G f i)`.

```lean
Ring.DirectLimit.henselianRing.{u_1, u_2} {ι : Type u_1} [Preorder ι] {G : ι → Type u_2}
  [(i : ι) → CommRing (G i)] {f : (i j : ι) → i ≤ j → G i →+* G j} {I : (i : ι) → Ideal (G i)}
  [Nonempty ι] [IsDirectedOrder ι] [DirectedSystem G fun x1 x2 x3 => ⇑(f x1 x2 x3)]
  [∀ (i : ι), HenselianRing (G i) (I i)]
  (hI : ∀ (i j : ι) (hij : i ≤ j), I i ≤ Ideal.comap (f i j hij) (I j)) :
  HenselianRing (Ring.DirectLimit G fun x1 x2 x3 => ⇑(f x1 x2 x3))
    (⨆ i, Ideal.map (Ring.DirectLimit.of G (fun x1 x2 x3 => ⇑(f x1 x2 x3)) i) (I i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ring.DirectLimit.henselianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/DirectLimit.html#Ring.DirectLimit.henselianRing).

## Sources

- [Tau Ceti documentation: `Ring.DirectLimit.henselianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselian/DirectLimit.html#Ring.DirectLimit.henselianRing)
- [Source of `Ring.DirectLimit.henselianRing` in TauCeti/RingTheory/Henselian/DirectLimit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Henselian/DirectLimit.lean#L47)
- [Tau Ceti roadmap status: Analytic adic geometry for diamonds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicEtaleGeometry/STATUS.md)
