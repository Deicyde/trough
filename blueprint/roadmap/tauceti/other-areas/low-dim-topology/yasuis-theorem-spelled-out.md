---
declaration: theorem
origin: cited
lean: TauCeti.yasuiTheorem_iff
statement: formalized
proof: formalized
---

# Yasui's theorem spelled out

there are knots `K K' : S¹ → S³` with `0`-surgeries `Y`, `Y'`,
oriented compatibly with an orientation of `S³`, and an orientation-preserving homeomorphism
`Y ≃ₜ Y'`, such that `K` is smoothly concordant neither to `K'` nor to its reverse.

```lean
TauCeti.yasuiTheorem_iff :
  TauCeti.YasuiTheorem ↔
    ∃ o K K' Φ Φ',
      ∃ (h : TauCeti.IsSolidTorusNeighborhood (⇑K) Φ) (h' :
        TauCeti.IsSolidTorusNeighborhood (⇑K') Φ'),
        ∃ Y Y' x,
          ∃ (x_1 : T2Space Y),
            ∃ x_2 x_3,
              ∃ (x_4 : T2Space Y'),
                ∃ x_5 F F' oY oY' e,
                  F.IsOrientationCompatible o oY ∧
                    F'.IsOrientationCompatible o oY' ∧
                      oY'.comap ⋯ = oY ∧
                        ¬TauCeti.SmoothEmbedding.Concordant K K' ∧
                          ¬TauCeti.SmoothEmbedding.Concordant K K'.reverse
```

## Depends on

- [The Hurewicz theorem](../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)
- [TauCeti.IsSolidTorusNeighborhood.framingNumber](../../geometry/part-01/geometric-topology-and-the-solved-kirby-list-pro/tauceti-issolidtorusneighborhood-framingnumber.md)
- [TauCeti.knotExterior](../../geometry/part-01/geometric-topology-and-the-solved-kirby-list-pro/tauceti-knotexterior.md)

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../algebraic-topology/singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.yasuiTheorem_iff`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/AkbulutKirby.html#TauCeti.yasuiTheorem_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.yasuiTheorem_iff`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/AkbulutKirby.html#TauCeti.yasuiTheorem_iff)
- [Source of `TauCeti.yasuiTheorem_iff` in TauCeti/LowDimTopology/DehnSurgery/AkbulutKirby.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LowDimTopology/DehnSurgery/AkbulutKirby.lean#L143)
