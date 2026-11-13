---
declaration: section
origin: cited
lean: OAI.Thorp.Current.first_reciprocal_main, OAI.ThorpResults.remaining_main, OAI.PartialPermutation.complementaryCosets_finite, OAI.ThorpNine.main, OAI.RowColumn.occupied_overlap_endpoint, OAI.RowColumn.occupied_overlap, OAI.CubeShuffle.WeightedSweep.weighted_sweep_moments, OAI.ThorpNine.Harmonic.Thorp.LowPlanes.regular_trace_smoothing
statement: formalized
proof: formalized
---

# 238. Optimal logarithmic mixing of the Thorp shuffle

12 manuscripts and 15 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the Thorp shuffle randomizes $N=2^d$ labeled cards in $\Theta(\log N)$ physical shuffles, settling its optimal mixing order for power-of-two deck sizes. Convergence is in total variation from the worst initial ordering and concerns the entire permutation, not just individual card positions.

## Optimal-order mixing of the Thorp shuffle

We prove that the Thorp shuffle on $2^d$ cards mixes in $\Theta(d)$ complete shuffles. The full permutation law after $1600d$ shuffles converges to uniform in total variation as $d\to\infty$, uniformly over the initial deck, while a support count gives a lower bound of $2d-O(1)$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Optimal-order-mixing-of-the-Thorp-shuffle-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Random coordinate frames and partial permutation laws

For the Thorp shuffle on $2^d$ cards, we prove that the worst-start total-variation distance after $32800d$ physical shuffles tends to zero as $d\to\infty$. Combining our fixed-list estimate with the companion Fourier transfer improves this bound to $512d$ shuffles. These results follow from bounds on partially observed permutation laws in random coordinate frames.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Random-coordinate-frames-and-partial-permutation-laws-September-26-2026/main.pdf).

## From partial permutation information to Fourier bounds

We show how information about partial permutations controls full permutation laws. Let *n* tend to infinity through multiples of eight. If the images of a uniformly chosen $7n/8$ labels approach the uniform injection law in average total variation, and the sign mean tends to zero, then the product of two independent permutations with the given law converges to uniform on $S_{n}$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/From-partial-permutation-information-to-Fourier-bounds-September-26-2026/main.pdf); the Lean below formalizes results from it.

## Conditional information under deterministic coordinate sweeps

We bound the information remaining after paths of specified cards in the Thorp shuffle on $n=2^d$ cards have been observed. After a fixed number of deterministic coordinate sweeps, the joint endpoint law of further cards is close to uniform on the available positions, on average over the observed paths, provided a fixed positive fraction of labels lies outside both lists. Combined with a Fourier transfer, these bounds give full-deck mixing after $2048d$ physical shuffles.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Conditional-information-under-deterministic-coordinate-sweeps-September-26-2026/main.pdf).

## Conditional permutations in a revealed switching environment

Fix half the labels in a Thorp shuffle on $2^d$ positions and reveal their complete trajectories. We prove that, after an explicit absolute number of coordinate sweeps, the conditional permutation of the remaining labels approaches uniform in expected total variation as $d\to\infty$, uniformly in the initial layout. The resulting constructions give full-deck mixing in a constant multiple of *d* physical shuffles.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Conditional-permutations-in-a-revealed-switching-environment-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Routing densities and representation contraction for Thorp sweeps

For $N=2^d$ cards, we prove that an absolute number of coordinate sweeps of the Thorp shuffle brings the full permutation law to total-variation distance tending to zero from uniform. The mixing time therefore has optimal order $\Theta(\log N)$ in physical shuffles.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Routing-densities-and-representation-contraction-for-Thorp-sweeps-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Row–column symmetry and contraction of coordinate sweeps

We prove that the Thorp shuffle on $N=2^d$ labeled cards has full-permutation total-variation mixing time $\Theta(\log N)$ in physical shuffles. An absolute number of coordinate sweeps suffices for the upper bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Row-column-symmetry-and-contraction-of-coordinate-sweeps-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Random-subspace tests and trace smoothing for coordinate sweeps

We prove that an absolute number of coordinate sweeps of the Thorp shuffle on $n=2^d$ positions brings the full permutation to total-variation distance at most $\frac12n^{-5}$ from uniform, uniformly over the initial deck. Thus $O(d)$ physical shuffles suffice, which is optimal in order.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Random-subspace-tests-and-trace-smoothing-for-coordinate-sweeps-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Compatibility entropy and the spectrum of a Thorp sweep

We prove that the Thorp shuffle on $n=2^d$ cards mixes in $\Theta(d)$ physical shuffles. After a sufficiently large fixed number of coordinate sweeps, the total-variation distance of the full permutation from uniform tends to zero as $d\to\infty$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Compatibility-entropy-and-the-spectrum-of-a-Thorp-sweep-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Signed tensor densities and diagram budgets for the Thorp shuffle

We prove that a fixed number of coordinate sweeps of the Thorp shuffle on $2^d$ cards makes the squared $L^{2}$ distance of the full permutation density from uniform tend to zero as $d\to\infty$. In particular, the total-variation mixing time is $\Theta(d)$ physical shuffles.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Signed-tensor-densities-and-diagram-budgets-for-coordinate-sweeps-September-26-2026/paper.pdf); the Lean below formalizes results from it.

## Conditional coordinate sweeps and analytic transfer

For coordinate sweeps with near-uniform line laws and line sizes among powers of two in a suitable fixed interval, we prove a Schatten-moment bound after conditioning on any feasible collection of prescribed card trajectories. An analytic transfer to binary sweeps then shows that a fixed number of sweeps mixes the Thorp shuffle on $2^d$ cards in $O(d)$ physical steps, matching the order of the support lower bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Conditional-coordinate-sweeps-and-analytic-transfer-September-26-2026/main.pdf); the Lean below formalizes results from it.

## A strict four-row permanent inequality and permutation moments

We prove a permanent inequality with exponent strictly below two for laws on $S_{4}$ sufficiently close to uniform and with exactly uniform coordinate marginals. Applied to a four-row recursion, it shows that an absolute number of coordinate sweeps brings the full permutation of the Thorp shuffle on $N=2^d$ cards to total-variation distance tending to zero from uniform as $N\to\infty$. Thus the mixing time has the optimal order $O(\log N)$ in physical shuffles.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-strict-four-row-permanent-inequality-and-permutation-moments-September-26-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves optimal-order mixing of the Thorp shuffle on $2^d$ cards. After $1600d$ complete shuffles, the full permutation law converges in total variation to uniform as $d\to\infty$, uniformly over initial decks. Together with the support lower bound of $2d-O(1)$, this gives mixing time $\Theta(d)=\Theta(\log(2^d))$.

The linked supporting results include frame and conditional-list estimates, regular trace and spectral bounds, signed moments, and full-density $L^2$ control. They also bound reciprocal Specht-dimension sums and give the eight-block Fourier estimate used in the mixing argument.

The formalized supporting result turns bounds on partial-permutation cosets into Fourier bounds. Partition a finite set into $b\ge1$ nonempty blocks, and let $f\ge0$ be a subprobability weight on its symmetric group whose left-coset masses for each block subgroup are at most $B$. For every irreducible unitary representation of dimension $D$ and every $u>0$, both the squared Hilbert–Schmidt norm and squared operator norm of its Fourier transform are at most $bB\,C(u)D^{-1+(u+2)/b}$, where $C(u)$ is the stated symmetric-group degree constant.

The paper's asymptotic conclusion about the product of two random permutations is outside this selected finite estimate.

The formalized results give averaged conditional mixing for half-permutations in the revealed-path model and full-deck mixing for the Thorp shuffle. In particular, the full-deck total-variation distance tends to zero after $16040400d$ steps on $2^d$ cards, uniformly over deterministic initial decks. The conditional estimate is averaged over the actual outside-path law, rather than asserted for each individual environment. The formalization also includes the associated overlay, reset minorization, and two-color conditional constructions.

The formalization covers nine routing and representation estimates for Thorp sweeps: adaptive operator and fourth-trace bounds, Casimir moments, dense truncation, sparse contact, harmonic-cycle contraction, smoothing, and three tail or sparse-saving estimates. They bound routing-density deviations and Fourier operators in dense and sparse regimes, including exponential savings in the level scale and representation dimension.

The conditional high-height estimate requires a sufficiently large cutoff height $J$ that exceeds twice the number $s$ of coordinates in the fixed low block, so $J>2s$. These are the earlier nine statements associated with the paper; its changed later statements and six other result blocks are outside this scope.

The formalization proves uniform representation bounds for one coordinate sweep of the Thorp shuffle. For each irreducible representation of dimension $D$, it chooses a weight between $D^{3/4}$ and $D$ and a Schatten exponent bounded by one absolute constant so that the weighted Schatten moment is at most one. The sweep's operator norm is consequently at most $D^{-c}$ for one absolute $c>0$.

The supporting row–column estimate bounds the total squared overlap over all multiplicity copies on an occupied board, with explicit dependence on the row and column representation dimensions, the global dimension, the number of missing cells, and the number of rows or columns containing the global Young diagram. The paper's full physical-mixing conclusion is outside these selected representation estimates.

The formalization proves a uniform trace-smoothing estimate for coordinate sweeps of the Thorp shuffle on $2^d$ cards. One absolute sweep parameter works for every $d\ge1$: the regular trace is at most $1+(2^d)^{-10}$, and the full permutation law after the corresponding fixed number of sweeps is within $\tfrac12(2^d)^{-5}$ of uniform in total variation, for every initial deck. Thus the selected upper bound uses $O(d)$ physical shuffles.

The formalized result is the weighted compatibility theorem for balanced $A\times D$ rectangles, with $n=AD$ and $\sqrt n/2\le A,D\le2\sqrt n$. For arbitrary nonnegative weights on the row and column permutation groups, the normalized compatibility average is bounded by $\exp(C_0n^{54/100})$ times the product of the marginal $L^{1/\theta}$ factors, where $\theta=1-L/\log\sqrt n>0$ and the constants are absolute. Compatibility means injectivity in every original column. The bounded regular-moment and other moment/rank conclusions are not included.

The formalization gives signed representation estimates for coordinate sweeps of the Thorp shuffle. For every signed occurrence of a Young diagram of size $2^d$, it bounds the logarithm of a fixed-order weighted sweep moment by a small multiple of the signed partition entropy plus an explicit remainder-size budget. The moment order is uniform over the diagrams and decompositions after the two small coefficients are fixed.

The linked supporting angle bound controls the overlap of row, column, and global signed-type projections on an occupied rectangle, with explicit entropy, dimension, and missing-cell factors. These selected estimates support the paper's full-density argument; the full $L^2$ and total-variation mixing conclusion is outside them.

The formalized binary-sweep theorem gives a universal power contraction in every irreducible representation: for sufficiently large $d$, the averaged sweep on $2^d$ slots has operator norm at most $D^{-g}$ in representation dimension $D$, for some $g>0$. The sign expectation is zero, and a fixed number of independent sweeps approaches uniform in total variation from every initial deck. A separate conditional moment estimate covers allowed power-of-two grids and disjoint coordinate-respecting trajectories, with its stated feasibility premise. Physical-shuffle law identification is not included.

The formalization proves the paper's strict four-row permanent inequality. There are constants $4/3<p<2$ and $\varepsilon>0$ such that every probability law on $S_4$ within total-variation distance $\varepsilon$ of uniform, and with exactly uniform coordinate marginals, satisfies the permanent bound by the product of the four $L^p$ row norms for every nonnegative matrix. The exponent and neighborhood are uniform over those laws. The Thorp mixing consequence is outside this selected statement.

## Lean: Reciprocal Specht degrees and eight-block Fourier bound

```lean
theorem first_reciprocal_main :
    (BddAbove (Set.range (fun n : {n : ℕ // 1 ≤ n} => reciprocalFirst n.val)) ∧
    (∀ n : ℕ, 1 ≤ n → reciprocalFirst n ≤ C1) ∧
    Tendsto exceptionalFirst atTop (nhds 0)) ∧
    (∀ (d : ℕ) (_hd : 3 ≤ d)
    (e : Position d ≃ Fin 8 × Fin (2 ^ (d - 3)))
    {E : Type uE} [NormedAddCommGroup E] [InnerProductSpace ℂ E]
    [FiniteDimensional ℂ E]
    (ρ : Representation ℂ (Equiv.Perm (Position d)) E)
    [Representation.IsIrreducible ρ]
    (_ : ∀ g x y, ⟪ρ g x, ρ g y⟫_ℂ = ⟪x, y⟫_ℂ)
    (ν : Equiv.Perm (Position d) → ℝ)
    (_ : ∀ g, 0 ≤ ν g) (_ : ∑ g, ν g = 1)
    (_ : ∀ (i : Fin 8) (g : Equiv.Perm (Position d)),
      ∑ h : Equiv.Perm (Fin (2 ^ (d - 3))),
          ν (g * Block.embedding e (Pi.mulSingle i h)) ≤
        4 * (Fintype.card (Equiv.Perm (Fin (2 ^ (d - 3)))) : ℝ) /
          Fintype.card (Equiv.Perm (Position d))),
    ‖LinearMap.toContinuousLinearMap (Fourier.integrated ρ (fun g => (ν g : ℂ)))‖ ≤
      Real.sqrt (32 * C1) * (Module.finrank ℂ E : ℝ) ^ (-5 / 16 : ℝ))
```

Stated in [ThorpFirstReciprocal.lean, line 205](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThorpFirstReciprocal.lean#L205). Proved in [lean/OAI/Probability/ThorpShuffle/FirstMain.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThorpShuffle/FirstMain.lean#L13).

## Lean: Frame, spectral, and density estimates for Thorp mixing

```lean
theorem remaining_main :
    FrameMain ∧ InformationMain ∧ SpectrumMain ∧ SignedMain ∧
      DegreeSavingMain ∧ FullDensityMain ∧ ForwardMixingMain ∧ OptimalOrderMain
```

Stated in [ThorpRemaining.lean, line 543](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThorpRemaining.lean#L543). Proved in [lean/OAI/Probability/ThorpResults/Main.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThorpResults/Main.lean#L8).

## Lean: Fourier bounds from complementary coset caps

```lean
theorem complementaryCosets_finite : ComplementaryCosetsFiniteStatement
```

Stated in [PartialPermutation.lean, line 110](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PartialPermutation.lean#L110). Proved in [lean/OAI/RepresentationTheory/PartialPermutation/Main.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/PartialPermutation/Main.lean#L11).

## Lean: Nine routing-density and representation estimates

```lean
theorem ThorpNine.main :
    ThorpNine.Adaptive.Thorp.AdaptiveBounds.MainStatement ∧
    ThorpNine.Casimir.Thorp.CasimirBounds.MainStatement ∧
    ThorpNine.Dense.Thorp.DenseTruncation.MainStatement ∧
    ThorpNine.Contact.Thorp.SparseContact.MainStatement ∧
    ThorpNine.Harmonic.Thorp.HarmonicBounds.MainStatement ∧
    ThorpNine.Smoothing.Thorp.StrongSmoothing.MainStatement ∧
    ThorpNine.Tail.Thorp.StrongTail.MainStatement ∧
    ThorpNine.HighTail.Thorp.HighHeight.MainStatement ∧
    ThorpNine.SparseSaving.Thorp.SparseRegime.MainStatement
```

Stated in [ThorpRouting.lean, line 2567](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThorpRouting.lean#L2567). Proved in [lean/OAI/Probability/ThorpRouting/Main.lean, line 13](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThorpRouting/Main.lean#L13). formalization.yaml lists it as one of the repository's main results.

## Lean: Row–column overlap on occupied boards

```lean
theorem RowColumn.occupied_overlap_endpoint : RowColumn.OccupiedOverlapEndpoint
```

Stated in [OccupiedOverlap.lean, line 260](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OccupiedOverlap.lean#L260). Proved in [lean/OAI/RepresentationTheory/RowColumn/Occupied.lean, line 203](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/RowColumn/Occupied.lean#L203).

```lean
theorem RowColumn.occupied_overlap : RowColumn.OccupiedOverlapEndpoint
```

Stated in [OccupiedOverlap.lean, line 263](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/OccupiedOverlap.lean#L263). Proved in [lean/OAI/RepresentationTheory/RowColumn/Occupied.lean, line 274](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/RowColumn/Occupied.lean#L274).

## Lean: Weighted Schatten moments and operator contraction for coordinate sweeps

```lean
theorem weighted_sweep_moments :
    ∃ (W : YoungDiagram → ℝ) (pStar : ℝ) (p : ℕ → ℝ),
      (∀ μ : YoungDiagram, 0 < W μ) ∧
      2 ≤ pStar ∧
      (∀ d : ℕ, 1 ≤ d → 2 ≤ p d ∧ p d ≤ pStar) ∧
      ∀ d : ℕ, 1 ≤ d → ∀ μ : Shapes (2 ^ d),
        dimension μ.1 ^ (3 / 4 : ℝ) ≤ W μ.1 ∧
        W μ.1 ≤ dimension μ.1 ∧
        W μ.1 *
          schattenNorm (V := hilbertSpace μ.1) (fourierSweep d μ) (p d) ^ (p d) ≤ 1 ∧
        ‖fourierSweep d μ‖ ≤ dimension μ.1 ^ (-3 / (4 * pStar))
```

Stated in [WeightedSweepMoments.lean, line 287](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/WeightedSweepMoments.lean#L287). Proved in [lean/OAI/Probability/CubeShuffle/WeightedMoments.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/CubeShuffle/WeightedMoments.lean#L19).

## Lean: Regular trace smoothing and full-permutation mixing

```lean
theorem regular_trace_smoothing : MainStatement
```

Stated in [CoordinateTrace.lean, line 366](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoordinateTrace.lean#L366). Proved in [lean/OAI/Probability/ThorpRouting/RegularTrace.lean, line 69](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThorpRouting/RegularTrace.lean#L69).

## Lean: Weighted row–column compatibility bound

```lean
theorem weightedCompatibility_main : WeightedCompatibilityTheorem
```

Stated in [ThorpWeightedCompatibility.lean, line 47](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/ThorpWeightedCompatibility.lean#L47). Proved in [lean/OAI/Probability/ThorpCompatibility/Main.lean, line 109](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/ThorpCompatibility/Main.lean#L109). formalization.yaml lists it as one of the repository's main results.

## Lean: One-sided angle bound for signed spin types

```lean
theorem one_sided_type_angle (W : Finset (R × C))
    (D : TypeLabel q) (H : C → TypeLabel q) (K : R → TypeLabel q)
    (hD : D.size = W.card)
    (hH : ∀ j, (H j).size = Fintype.card (TypeBlocks.Fiber (column W) j))
    (hK : ∀ i, (K i).size = Fintype.card (TypeBlocks.Fiber (row W) i)) :
    (‖TypeBlocks.projection (column W) H * TypeBlocks.projection (row W) K * D.projection W‖ ^ 2 ≤
      min 1 (Real.exp (TypeBlocks.entropy H + TypeBlocks.entropy K - D.entropy) *
        (TypeBlocks.dimension H : ℝ) * (TypeBlocks.dimension K : ℝ) * phi W)) ∧
    (min 1 (Real.exp (TypeBlocks.entropy H + TypeBlocks.entropy K - D.entropy) *
        (TypeBlocks.dimension H : ℝ) * (TypeBlocks.dimension K : ℝ) * phi W) ≤
      min 1 (Real.exp (TypeBlocks.entropy H + TypeBlocks.entropy K - D.entropy +
        (Fintype.card R * Fintype.card C - W.card : ℕ)) *
        (TypeBlocks.dimension H : ℝ) * (TypeBlocks.dimension K : ℝ))) ∧
    TypeBlocks.dimension H * TypeBlocks.dimension K ≤
      (W.card + 1) ^ ((Fintype.card R + Fintype.card C) * q * (q - 1))
```

Stated in [SpinAngle.lean, line 521](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SpinAngle.lean#L521). Proved in [lean/OAI/RepresentationTheory/SpinAngle/TypeAngle.lean, line 189](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/RepresentationTheory/SpinAngle/TypeAngle.lean#L189).

## Lean: Uniform signed-occurrence moment bound for coordinate sweeps

```lean
theorem signed_occurrence_moment_bound :
    ∃ η₀ : ℝ, 0 < η₀ ∧
      ∀ η : ℝ, 0 < η → η < η₀ →
        ∃ κ₀ : ℝ, 0 < κ₀ ∧ κ₀ < η / 256 ∧
          ∀ κ : ℝ, 0 < κ → κ < κ₀ →
            ∃ r : ℕ, 1 ≤ r ∧
              ∀ d : ℕ, 1 ≤ d →
                ∀ lam : Partition (2 ^ d),
                  ∀ (u v l : ℕ) (h : u + v + l = 2 ^ d)
                    (α : Partition u) (β : Partition v) (γ : Partition l),
                    SignedOccurrence h α β γ lam →
                      logMoment (weightedMoment lam r) ≤
                        ((coefficient η d * signedEntropy α β +
                            remainderBudget κ d l : ℝ) : EReal)
```

Stated in [SignedSweepMoment.lean, line 169](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SignedSweepMoment.lean#L169). Proved in [lean/OAI/Probability/SignedSweeps/UniformMoment.lean, line 128](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/SignedSweeps/UniformMoment.lean#L128).

## Lean: Binary sweep contraction and mixing

```lean
theorem binary_sweep_contraction_and_mixing :
    BinaryCoordinateSweeps.BinaryContractionTarget ∧
    (∀ d : ℕ, 0 < d → ∑ g : Equiv.Perm (BinaryCoordinateSweeps.Slot d),
      BinaryCoordinateSweeps.binaryLaw d g * BinaryCoordinateSweeps.realSign g = 0) ∧
    BinaryCoordinateSweeps.UniformSweepMixingTarget
```

Stated in [BinarySweep.lean, line 95](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BinarySweep.lean#L95). Proved in [lean/OAI/Probability/BinarySweep/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/BinarySweep/Main.lean#L10). formalization.yaml lists it as one of the repository's main results.

## Lean: Conditional coordinate-sweep moment estimate

```lean
theorem conditional_main : ConditionalMain
```

Stated in [CoordinateSweeps.lean, line 307](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoordinateSweeps.lean#L307). Proved in [lean/OAI/Probability/CoordinateSweeps/Main.lean, line 454](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/CoordinateSweeps/Main.lean#L454). formalization.yaml lists it as one of the repository's main results.

```lean
theorem all_grid_moment {r : ℕ} (hr : ScaleLarge r) (hrS : SparseScalar.ScaleReady r)
    (hS : ∀ G : Grid, G.Allowed r → ScalarInduction.MainSizeReady SparseScalar.q G.size)
    {zStar : ℝ} (hζ : SparsePerturb r zStar) {z : ℝ} (hz : z∈Set.Icc 0 zStar) :
    ∀ G : Grid, G.Allowed r → MomentBound G SparseScalar.q z
```

Stated in [CoordinateSweeps.lean, line 300](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CoordinateSweeps.lean#L300). Proved in [lean/OAI/Probability/CoordinateSweeps/Main.lean, line 412](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/CoordinateSweeps/Main.lean#L412).

## Lean: Strict four-row permanent inequality near the uniform law

```lean
theorem robust_permanent :
  ∃ p₀ : ℝ, 4 / 3 < p₀ ∧ p₀ < 2 ∧
    ∃ ε : ℝ, 0 < ε ∧ ∀ ν : Law,
      IsProbability ν → totalVariation ν < ε → UniformMarginals ν →
      ∀ f : Functions, (∀ i j, 0 ≤ f i j) →
        permanentExpectation ν f ≤ ∏ i, lpNorm p₀ (f i)
```

Stated in [FourRowPermanent.lean, line 37](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FourRowPermanent.lean#L37). Proved in [lean/OAI/Combinatorics/Permanent/Main.lean, line 100](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/Permanent/Main.lean#L100).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/238.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/238.md)
