---
declaration: section
origin: cited
lean: OAI.DukePrimeDegree.prime_degree_packet_measure_equidistribution_unconditional, OAI.DukePrimeDegree.prime_degree_packet_measures_tendsto_haar_unconditional
statement: formalized
proof: formalized
---

# 015. Torus-packet equidistribution in prime, quartic, and sextic degrees

3 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Haar equidistribution without escape of mass for complete volume-weighted torus packets from totally real fields: arbitrary lattices and prescribed local types in fixed prime degree at least five, arbitrary-order Picard packets in primitive quartic fields, and maximal-order ideal-class packets in primitive sextic fields. Here primitive means having no proper intermediate field; the relevant order or field discriminant tends to infinity.

## Equidistribution of Prime-Degree Torus Packets with Arbitrary Local Type

We prove the packet form of the higher-dimensional Duke equidistribution problem for totally real fields of any fixed prime degree at least five, allowing arbitrary local homothety types of full lattices. As the multiplier-order discriminant tends to infinity, the volume-weighted packet measures converge to Haar probability measure, with no escape of mass.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Equidistribution-of-Prime-Degree-Torus-Packets-with-Arbitrary-Local-Type-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## Equidistribution of primitive quartic torus packets for arbitrary orders

Let *K* range over totally real quartic fields with no proper intermediate field, and let $\mathcal O$ be any order in *K*. We prove that the packets of periodic diagonal orbits attached to invertible $\mathcal O$-ideal classes, weighted by orbit volume, equidistribute with no escape of mass as $|\mathop{\mathrm{Disc}}\nolimits (\mathcal O)|$ tends to infinity. The proof combines measure rigidity with a cubic-resolvent estimate that remains uniform at primes dividing the order index.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf).

## Equidistribution of Primitive Sextic Torus Packets

We prove that the complete ideal-class packets of maximal orders in totally real sextic fields with no proper intermediate fields become equidistributed, with no escape of mass, in the space of unimodular lattices as their field discriminants tend to infinity. The limit is Haar probability measure. Each packet includes all coordinate-sign translates and is weighted by diagonal-orbit volume.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Equidistribution-of-Primitive-Sextic-Torus-Packets-October-5-2026/primitive-sextic-torus-packets.pdf).

## The Lean formalization

The formalization proves equidistribution of volume-weighted torus packets for totally real number fields of every fixed prime degree at least five. For any sequence of full lattices whose multiplier-order discriminants tend to infinity, the packet measures converge weakly to Haar probability measure and form a tight family, so no mass escapes. Arbitrary local homothety types are allowed, and the fields may vary along the sequence.

## Lean: Equidistribution of prime-degree torus packets

```lean
theorem prime_degree_packet_measure_equidistribution_unconditional
    (d : ℕ) (hprime : Nat.Prime (d+1)) (hfive : 5 ≤ d+1)
    (K : ℕ → Type u) [∀ i, Field (K i)] [∀ i, NumberField (K i)]
    [∀ i, NumberField.IsTotallyReal (K i)]
    (M : ∀ i, PrimeDegreePackets.FullLattice (d+1) (K i))
    (σ : ∀ i, OrderedEmbeddings (d+1) (K i))
    (hn : ∀ i, Module.finrank ℚ (K i)=d+1)
    (hD : Tendsto (fun i => PrimeDegreePackets.multiplierDiscriminant (M i)) atTop atTop) :
    ∃ ν : Measure (X (d+1)), IsHaarProbability ν ∧
      WeakProbabilityConvergence (fun i => packetMeasure (M i) (σ i)) ν ∧
      IsTightMeasureSet (Set.range (fun i => packetMeasure (M i) (σ i)))
```

Stated in [DukePrimeDegree.lean, line 200](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DukePrimeDegree.lean#L200). Proved in [lean/OAI/NumberTheory/DukePrimeDegree/MainUnconditional.lean, line 60](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/DukePrimeDegree/MainUnconditional.lean#L60).

```lean
theorem prime_degree_packet_measures_tendsto_haar_unconditional
    (d : ℕ) (hprime : Nat.Prime (d+1)) (hfive : 5 ≤ d+1)
    (K : ℕ → Type u) [∀ i, Field (K i)] [∀ i, NumberField (K i)]
    [∀ i, NumberField.IsTotallyReal (K i)]
    (M : ∀ i, PrimeDegreePackets.FullLattice (d+1) (K i))
    (σ : ∀ i, OrderedEmbeddings (d+1) (K i))
    (hn : ∀ i, Module.finrank ℚ (K i)=d+1)
    (hD : Tendsto (fun i => PrimeDegreePackets.multiplierDiscriminant (M i)) atTop atTop)
    (m : ProbabilityMeasure (X (d+1)))
    (hm : IsHaarProbability (m : Measure (X (d+1)))) :
    WeakProbabilityConvergence (fun i => packetMeasure (M i) (σ i))
      (m : Measure (X (d+1)))
```

Stated in [DukePrimeDegree.lean, line 215](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DukePrimeDegree.lean#L215). Proved in [lean/OAI/NumberTheory/DukePrimeDegree/MainUnconditional.lean, line 80](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/DukePrimeDegree/MainUnconditional.lean#L80).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/015.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/015.md)
