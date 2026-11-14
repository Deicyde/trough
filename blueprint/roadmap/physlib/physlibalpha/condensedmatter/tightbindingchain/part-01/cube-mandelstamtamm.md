---
declaration: module
origin: cited
lean: CondensedMatter.TightBindingChain.mandelstamTammRatio_alongX, CondensedMatter.TightBindingChain.mandelstamTammRatio_alongY, CondensedMatter.TightBindingChain.mandelstamTammRatio_alongZ
statement: formalized
proof: formalized
---

# Mandelstam–Tamm and Cramér–Rao on the open tight binding cube

The module `PhyslibAlpha.CondensedMatter.TightBindingChain.Cube.MandelstamTamm`, [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean): 3 declarations, 3 with a docstring.

## i. Overview

> In the maximal current state of the cube, each axis sees only its own chain, so the
> Mandelstam–Tamm ratio `⟨J⟩² / (4 Var H · Var X)` of an axis is the ratio `1 / C²` of the maximal
> current state of that chain.

## ii. Key results

> - `mandelstamTammRatio_alongX` (and `Y`, `Z`) : each axis of the cube has the ratio of its chain.

## iv. References

> * https://www.damtp.cam.ac.uk/user/tong/aqm/aqmtwo.pdf. [ref: tong\_statistical\_physics]

## A. The Mandelstam–Tamm ratio along each axis

**`CondensedMatter.TightBindingChain.mandelstamTammRatio_alongX`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean#L50).

> Along `x`, the maximal current state of the cube has the ratio `1 / C²` of `Tx`.

```lean
lemma mandelstamTammRatio_alongX :
    (Tx.maxCurrentCubeVectorState Ty Tz)⟨Tx.alongX Ty Tz Tx.currentObservable⟩ ^ 2 /
      (4 * (variance (Tx.maxCurrentCubeVectorState Ty Tz)
          (Tx.alongX Ty Tz Tx.openHamiltonianObservable) *
        variance (Tx.maxCurrentCubeVectorState Ty Tz)
          (Tx.alongX Ty Tz Tx.positionObservable))) = 1 / Tx.uncertaintyRatio ^ 2
```

**`CondensedMatter.TightBindingChain.mandelstamTammRatio_alongY`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean#L64).

> Along `y`, the maximal current state of the cube has the ratio `1 / C²` of `Ty`.

```lean
lemma mandelstamTammRatio_alongY :
    (Tx.maxCurrentCubeVectorState Ty Tz)⟨Tx.alongY Ty Tz Ty.currentObservable⟩ ^ 2 /
      (4 * (variance (Tx.maxCurrentCubeVectorState Ty Tz)
          (Tx.alongY Ty Tz Ty.openHamiltonianObservable) *
        variance (Tx.maxCurrentCubeVectorState Ty Tz)
          (Tx.alongY Ty Tz Ty.positionObservable))) = 1 / Ty.uncertaintyRatio ^ 2
```

**`CondensedMatter.TightBindingChain.mandelstamTammRatio_alongZ`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean#L79).

> Along `z`, the maximal current state of the cube has the ratio `1 / C²` of `Tz`.

```lean
lemma mandelstamTammRatio_alongZ :
    (Tx.maxCurrentCubeVectorState Ty Tz)⟨Tx.alongZ Ty Tz Tz.currentObservable⟩ ^ 2 /
      (4 * (variance (Tx.maxCurrentCubeVectorState Ty Tz)
          (Tx.alongZ Ty Tz Tz.openHamiltonianObservable) *
        variance (Tx.maxCurrentCubeVectorState Ty Tz)
          (Tx.alongZ Ty Tz Tz.positionObservable))) = 1 / Tz.uncertaintyRatio ^ 2
```

## Depends on

- [The open tight binding cube](cube-basic.md)
- [Mandelstam–Tamm and Cramér–Rao in the open tight binding chain](current-mandelstamtamm.md)

## Proof depends on

- [Mandelstam–Tamm and Cramér–Rao in the maximal current state](maxcurrentstate-mandelstamtamm.md)

## Sources

- [PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/TightBindingChain/Cube/MandelstamTamm.lean)
