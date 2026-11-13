---
declaration: section
origin: cited
lean: Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.Config, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.rising, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.count, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdFamily, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdScore, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.predictive, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.seqProbAfter, Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.seqProb
statement: formalized
proof: formalized
---

# Markov equivalence and Bayesian network scores

21 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html).

## Joint configurations of a set of variables

The joint values of the variables in `S`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.Config`, an abbreviation declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#config).

## Rising factorial

The rising factorial `a (a + 1) ⋯ (a + n - 1)`, equal to `Γ(a + n) / Γ(a)` for `a > 0`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.rising`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#rising).

## Count of cases matching a configuration

The number of cases in `D` that take the values `c` on the variables `S`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.count`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#count).

## Bayesian–Dirichlet family score

The Bayesian–Dirichlet score of a family `F` with parent set `P ⊆ F` and hyperparameters
`α` on the configurations of `F`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdFamily`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bd-family).

## Bayesian–Dirichlet network score

The BD score of the structure `Pa` with family hyperparameters `α`: the product of the
family scores.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdScore`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bd-score).

## Sequential Pólya–Dirichlet prediction factor

The sequential Pólya–Dirichlet prediction factor for the case `x` after the cases `D`:
`∏_v (α_{v,c} + n_{v,c}) / (α_{v,j} + n_{v,j})`, with `c`, `j` the family and parent values of
`x` and `n` the counts in `D`. This is a genuine conditional probability only when `Pa` is a
DAG; for arbitrary parent maps (e.g. cycles or self-parents) the factors over all cases need
not sum to one.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.predictive`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#predictive).

## Sequential Pólya–Dirichlet product after prior cases

The sequential Pólya–Dirichlet product for the cases `D`, in order, after the cases `E`:
each case contributes its `predictive` factor given all cases before it. A genuine probability
of the data only when `Pa` is a DAG (see `predictive`).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.seqProbAfter`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#seq-prob-after).

## Sequential Pólya–Dirichlet product of the data

The sequential Pólya–Dirichlet product for the cases of `D`, in order. A genuine probability
of the data only when `Pa` is a DAG (see `predictive`).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.seqProb`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#seq-prob).

## Parent configuration counts sum over family configurations

The number of cases matching a parent configuration is the sum over the family
configurations extending it (`N_j = ∑_k N_jk`).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.sum_count_restrict₂`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#sum-count-restrict).

## The BD score is the sequential prediction product

**The BD score is the sequential prediction product** of the data (hence it does not
depend on the order of the cases). This is an identity for all real hyperparameters.
Positivity of the hyperparameters only makes every predictive denominator positive; it does
not make this product a probability. The product is a genuine probability of the data only
when `Pa` is a DAG with no self-parents: for cyclic parent maps the predictive factors over
all cases need not sum to one.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.seqProb_eq_bdScore`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#seq-prob-eq-bd-score).

## BDe hyperparameters

BDe hyperparameters (Heckerman, Geiger and Chickering): `ess` times the weight
`∑_{x ↦ c} p x` of the configuration `c` of `S`. When `∑ x, p x = 1`, `p` is a prior joint
distribution and this is the prior probability of `c`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdeHyper`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bde-hyper).

## BDe marginal likelihood of a variable set

The (unnormalized) marginal likelihood of the data restricted to the variables `S` under
the BDe Dirichlet prior on the joint values of `S`. `p` is treated as generalized weights
here: the total Dirichlet mass over configurations is `ess * ∑ x, p x`, so the omitted
normalizing factor is `1 / rising (ess * ∑ x, p x) D.length`, the same for every `S`. When
`p` is normalized (`∑ x, p x = 1`) this is `1 / rising ess D.length`, and `p` is a prior
joint distribution.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.margLik`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#marg-lik).

## BDe family score as a ratio of marginal likelihoods

With BDe hyperparameters, a family score is a ratio of set marginal likelihoods.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdFamily_bdeHyper`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bd-family-bde-hyper).

## BDe network score

The BDe score of the structure `Pa`.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdeScore`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bde-score).

## Covered-edge reversal

`Pa'` is obtained from `Pa` by reversing a covered edge `x → y` (Chickering 1995): `x` is a
parent of `y` and `y`'s other parents are exactly `x`'s parents (`Pa y = insert x (Pa x)`);
after the reversal `y` has parents `Pa x` and `x` has parents `insert y (Pa x)`. Acyclicity
is not required: the score identity holds for any parent-set maps (on a DAG, `x ∉ Pa x` and
`y ∉ Pa x` hold automatically).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.CoveredReversal`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#covered-reversal).

## Covered-edge reversal preserves the BDe score

**Covered-edge reversal preserves the BDe score** (for a positive weight function `p` —
a prior when `∑ x, p x = 1` — and positive equivalent sample size).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdeScore_coveredReversal`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bde-score-covered-reversal).

## Covered-edge reversals preserve the BDe score

Structures connected by a sequence of covered-edge reversals have the same BDe score.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.bdeScore_eq_of_reflTransGen`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/BayesianDirichletScore.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#bde-score-eq-of-refl-trans-gen).

## Acyclic network structure

The structure has no directed cycle.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.IsAcyclic`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#is-acyclic).

## Adjacent vertices in a network structure

`u` and `w` are adjacent (joined by an edge in either direction).

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.Adjacent`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#adjacent).

## V-structure in a directed graph

`u → w ← z` is a v-structure: two non-adjacent distinct parents of a common child.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.IsVStructure`, a definition declared in [CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#is-vstructure).

## Chickering's transformational characterization

**Chickering's transformational characterization** (1995): two acyclic structures on a finite
set of vertices with the same skeleton and the same v-structures (Markov equivalent by Verma
and Pearl) are connected by a sequence of covered-edge reversals.

Formalized by `Cslib.MachineLearning.GraphicalModels.BayesianDirichlet.reflTransGen_coveredReversal_of_markovEquivalent`, a theorem declared in [CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean, line 579](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/MachineLearning/GraphicalModels/MarkovEquivalence.lean#L579). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html#refl-trans-gen-covered-reversal-of-marko).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Markov equivalence and Bayesian network scores](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/machine-learning/probabilistic-graphical-models/markov-equivalence-and-bayesian-network-scores)
