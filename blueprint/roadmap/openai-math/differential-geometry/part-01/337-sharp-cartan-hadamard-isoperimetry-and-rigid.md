---
declaration: section
origin: cited
lean: OAI.SharpIntegralFillings.coefficient_optimal, OAI.CAT0Fillings.sharp_integral_filling
statement: formalized
proof: formalized
---

# 337. Sharp Cartan–Hadamard isoperimetry and rigidity

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves generalized Cartan–Hadamard isoperimetry in every dimension: in a complete simply connected manifold with sectional curvature at most *κ* ≤ 0, every finite-volume finite-perimeter set satisfies the sharp comparison with the equal-volume model ball. Bounded positive-volume equality regions for *κ* = 0 are Euclidean balls. Also proves sharp Euclidean filling bounds for compactly supported integral *n*-cycles, *n* ≥ 2, in arbitrary proper CAT$(0)$ spaces.

## Generalized Cartan–Hadamard isoperimetry and Euclidean equality rigidity

We resolve the generalized Cartan–Hadamard isoperimetric conjecture in every dimension. In a complete simply connected smooth manifold with sectional curvature at most *κ* ≤ 0, every finite-volume set of finite ambient perimeter has perimeter at least that of the equal-volume ball in curvature *κ*. For bounded positive-volume sets, equality in the Euclidean comparison holds precisely when the set agrees up to null sets with an open region isometric, with its induced metric, to a round Euclidean ball.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Generalized-Cartan-Hadamard-isoperimetry-and-Euclidean-equality-rigidity-September-23-2026/paper.pdf).

## Sharp integral fillings in CAT(0) spaces

Every compactly supported integral *n*-cycle, *n* ≥ 2, in a proper CAT(0) space bounds a compactly supported integral current with the sharp Euclidean mass bound. The theorem allows arbitrary integer multiplicities and unrestricted ambient dimension. In particular, we prove the Euclidean Cartan–Hadamard isoperimetric conjecture in dimensions at least three.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-integral-fillings-in-CAT%280%29-spaces-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves the sharp Euclidean filling inequality for every compactly supported integral $n$-cycle in a proper $\mathrm{CAT}(0)$ space, for $n\ge2$. It constructs a compactly supported integral filling whose mass is at most $C_n$ times the boundary mass to the power $(n+1)/n$, where $C_n$ is the Euclidean isoperimetric coefficient. Integer multiplicities and the ambient dimension are unrestricted.

A second statement proves that this coefficient is optimal by giving, in Euclidean space, a cycle for which every compactly supported integral filling has at least that mass. This yields the selected integral-current form of the Cartan–Hadamard isoperimetric conjecture.

## Lean: Optimality of the Euclidean filling coefficient

```lean
theorem coefficient_optimal (n : ℕ) (hn : 2 ≤ n) :
    ∃ T : IntegralCurrent (Euc (n + 1)) n,
      CompactlySupported T.val ∧ IsCycle T.val ∧ 0 < mass T.val ∧
      ∀ S : IntegralCurrent (Euc (n + 1)) (n + 1),
        CompactlySupported S.val → boundarySucc S.val = T.val →
        fillingCoefficient n * (mass T.val) ^ fillingPower n ≤ mass S.val
```

Stated in [FillingCoefficient.lean, line 120](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FillingCoefficient.lean#L120). Proved in [lean/OAI/Geometry/IntegralFillings/Main.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/IntegralFillings/Main.lean#L60).

## Lean: Sharp integral fillings in proper $\mathrm{CAT}(0)$ spaces

```lean
theorem sharp_integral_filling
    (X : Type u) [MetricSpace X] [MeasurableSpace X] [BorelSpace X] [ProperSpace X]
    (hX : IsCAT0 X) (n : ℕ) (hn : 2 ≤ n) (T : IntegralCurrent X n)
    (hTc : CompactlySupported T.val) (hTz : IsCycle T.val) :
    ∃ S : IntegralCurrent X (n + 1), CompactlySupported S.val ∧
      boundarySucc S.val = T.val ∧
      mass S.val ≤ fillingCoefficient n * (mass T.val) ^ fillingPower n
```

Stated in [SharpCAT0Filling.lean, line 135](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SharpCAT0Filling.lean#L135). Proved in [lean/OAI/Geometry/CAT0Fillings/Main.lean, line 111](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/CAT0Fillings/Main.lean#L111).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/337.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/337.md)
