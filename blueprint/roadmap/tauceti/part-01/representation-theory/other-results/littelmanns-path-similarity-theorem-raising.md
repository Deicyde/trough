---
declaration: theorem
origin: cited
lean: TauCeti.PLPath.raiseIter_map_natCast_smul, TauCeti.PLPath.lowerIter_map_natCast_smul
statement: formalized
proof: formalized
---

# Littelmann's path similarity theorem (raising)

for `f x = 2` and any positive integer `n`,
dilating a piecewise-linear path `p` by `n` intertwines `raise f x` with the `n`-fold iterate
`raiseIter f x n`.

```lean
TauCeti.PLPath.raiseIter_map_natCast_smul.{u_2, u_3} {𝕜 : Type u_2} {V : Type u_3} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] {f : Module.Dual 𝕜 V}
  {x : V} (hx : f x = 2) {n : ℕ} (hn : 0 < n) (p : TauCeti.PLPath 𝕜 V) :
  TauCeti.PLPath.raiseIter f x n (p.map (↑n • LinearMap.id)) =
    Option.map (fun x => x.map (↑n • LinearMap.id)) (TauCeti.PLPath.raise f x p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PLPath.raiseIter_map_natCast_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Similarity.html#TauCeti.PLPath.raiseIter_map_natCast_smul).

## Other forms

**Littelmann's path similarity theorem (lowering).** Formalized in Tau Ceti as [`TauCeti.PLPath.lowerIter_map_natCast_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Similarity.html#TauCeti.PLPath.lowerIter_map_natCast_smul).

```lean
TauCeti.PLPath.lowerIter_map_natCast_smul.{u_2, u_3} {𝕜 : Type u_2} {V : Type u_3} [Field 𝕜]
  [LinearOrder 𝕜] [IsStrictOrderedRing 𝕜] [AddCommGroup V] [_root_.Module 𝕜 V] {f : Module.Dual 𝕜 V}
  {x : V} (hx : f x = 2) {n : ℕ} (hn : 0 < n) (p : TauCeti.PLPath 𝕜 V) :
  TauCeti.PLPath.lowerIter f x n (p.map (↑n • LinearMap.id)) =
    Option.map (fun x => x.map (↑n • LinearMap.id)) (TauCeti.PLPath.lower f x p)
```

## Sources

- [Tau Ceti documentation: `TauCeti.PLPath.raiseIter_map_natCast_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/LSPath/Similarity.html#TauCeti.PLPath.raiseIter_map_natCast_smul)
- [Source of `TauCeti.PLPath.raiseIter_map_natCast_smul` in TauCeti/RepresentationTheory/LSPath/Similarity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/LSPath/Similarity.lean#L106)
