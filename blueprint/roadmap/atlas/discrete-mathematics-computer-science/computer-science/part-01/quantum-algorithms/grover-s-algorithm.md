---
declaration: section
origin: cited
lean: Cslib.Grover.Amplitude, Cslib.Grover.phaseOracle, Cslib.Grover.amplitudeNormSq, Cslib.Grover.markedProbability, Cslib.Grover.uniformAmplitude, Cslib.Grover.amplitudeNormSq_uniformAmplitude, Cslib.Grover.meanAmplitude, Cslib.Grover.diffusion
statement: formalized
proof: formalized
---

# Grover's algorithm

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html).

## Real amplitude vectors

For a type $\alpha$ (the search space), a real amplitude vector
indexed by $\alpha$ is a function $\psi : \alpha \to \mathbb{R}$, assigning a real amplitude to
each point of $\alpha$.

Formalized by `Cslib.Grover.Amplitude`, an abbreviation declared in [CSLibExt/Algorithms/Quantum/Grover/Basic.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Basic.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#amplitude).

## Phase oracle

For a type $\alpha$ and a finite set $M \subseteq \alpha$ of marked
elements, the phase oracle sends a real amplitude vector $\psi$ on $\alpha$ to the amplitude
vector whose value at $x$ is $-\psi(x)$ if $x \in M$ and $\psi(x)$ if $x \notin M$; that is, it
negates exactly the amplitudes at the marked elements.

Formalized by `Cslib.Grover.phaseOracle`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Basic.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Basic.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#phase-oracle).

## Squared norm of an amplitude vector

For a finite type $\alpha$ and a real amplitude
vector $\psi : \alpha \to \mathbb{R}$, the squared norm of $\psi$ is its squared Euclidean
norm $\sum_{x \in \alpha} \psi(x)^2$.

Formalized by `Cslib.Grover.amplitudeNormSq`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Basic.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Basic.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#amplitude-norm-sq).

## Probability of the marked outcomes

For a real amplitude vector $\psi$ on a type
$\alpha$ and a finite set $M \subseteq \alpha$ of marked elements, the marked probability is
$\sum_{x \in M} \psi(x)^2$. When $\alpha$ is finite and $\psi$ has squared norm $1$, this is
the probability of observing a marked outcome.

Formalized by `Cslib.Grover.markedProbability`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Basic.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Basic.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#marked-probability).

## Uniform amplitude vector

For a finite type $\alpha$, the uniform amplitude vector on
$\alpha$ is the real amplitude vector whose value at every point is $1/\sqrt{|\alpha|}$, where
$|\alpha|$ is the number of elements of $\alpha$.

Formalized by `Cslib.Grover.uniformAmplitude`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Basic.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Basic.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#uniform-amplitude).

## The uniform amplitude vector is normalized

For every nonempty finite type
$\alpha$, the uniform amplitude vector on $\alpha$ has squared Euclidean norm $1$.

Formalized by `Cslib.Grover.amplitudeNormSq_uniformAmplitude`, a theorem declared in [CSLibExt/Algorithms/Quantum/Grover/Basic.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Basic.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#amplitude-norm-sq-uniform-amplitude).

## Mean amplitude

For a finite type $\alpha$ and a real amplitude vector $\psi$ on $\alpha$,
the mean amplitude of $\psi$ is $\bigl(\sum_{x \in \alpha} \psi(x)\bigr) / |\alpha|$, the
arithmetic mean of its amplitudes. When $\alpha$ is empty it is $0$.

Formalized by `Cslib.Grover.meanAmplitude`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Diffusion.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Diffusion.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#mean-amplitude).

## Inversion about the mean

For a finite type $\alpha$, the diffusion operator sends a
real amplitude vector $\psi$ on $\alpha$ to the amplitude vector $x \mapsto 2\bar\psi - \psi(x)$,
where $\bar\psi$ is the arithmetic mean of the amplitudes of $\psi$.

Formalized by `Cslib.Grover.diffusion`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Diffusion.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Diffusion.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#diffusion).

## Grover step

Let $\alpha$ be a finite type and $M \subseteq \alpha$ a set of marked
elements. Write $O_M$ for the phase oracle, which negates the amplitudes at the points of $M$,
and $D$ for inversion about the mean, which sends an amplitude vector $\varphi$ on $\alpha$ to
$x \mapsto 2\bar\varphi - \varphi(x)$, where $\bar\varphi$ is the arithmetic mean of the amplitudes
of $\varphi$. One Grover step sends a real amplitude vector $\psi$ on $\alpha$ to $D(O_M \psi)$:
phase inversion followed by inversion about the mean.

Formalized by `Cslib.Grover.groverStep`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Diffusion.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Diffusion.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#grover-step).

## Symmetric amplitude vector

Let $M$ be a set of marked elements of a search space
$\alpha$, and let $a, b \in \mathbb{R}$. The symmetric amplitude vector with marked amplitude $a$
and unmarked amplitude $b$ is the real amplitude vector on $\alpha$ whose value is $a$ at every
element of $M$ and $b$ at every element outside $M$.

Formalized by `Cslib.Grover.symmetricAmplitude`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#symmetric-amplitude).

## Mean amplitude after the phase oracle

Let $M$ be a set of marked elements of a finite
search space of size $N$, let $M^c$ be the set of unmarked elements, and let $a, b \in \mathbb{R}$.
The oracle mean is $(|M^c|\, b - |M|\, a) / N$.

It is the mean of the amplitude vector obtained by applying the phase oracle to the vector equal
to $a$ on $M$ and to $b$ off $M$.

Formalized by `Cslib.Grover.oracleMean`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#oracle-mean).

## Marked amplitude after a Grover step

Let $M$ be a set of marked elements of a finite
search space of size $N$, let $M^c$ be the set of unmarked elements, and let $a, b \in \mathbb{R}$.
With $\mu = (|M^c|\, b - |M|\, a) / N$, the next marked amplitude is $2\mu + a$.

It is the common value at the marked elements after one Grover step applied to the amplitude
vector equal to $a$ on $M$ and to $b$ off $M$.

Formalized by `Cslib.Grover.markedAmplitudeNext`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#marked-amplitude-next).

## Unmarked amplitude after a Grover step

Let $M$ be a set of marked elements of a finite
search space of size $N$, let $M^c$ be the set of unmarked elements, and let $a, b \in \mathbb{R}$.
With $\mu = (|M^c|\, b - |M|\, a) / N$, the next unmarked amplitude is $2\mu - b$.

It is the common value at the unmarked elements after one Grover step applied to the amplitude
vector equal to $a$ on $M$ and to $b$ off $M$.

Formalized by `Cslib.Grover.unmarkedAmplitudeNext`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Symmetry.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#unmarked-amplitude-next).

## Grover angle

For a finite search space $\alpha$ and a marked set $M \subseteq \alpha$, the
Grover angle of $M$ is $\theta = \arcsin \sqrt{|M| / |\alpha|}$, where the quotient
$|M| / |\alpha|$ is taken to be $0$ when $\alpha$ is empty.

Formalized by `Cslib.Grover.groverAngle`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#grover-angle).

## Symmetric Grover state at a given angle

Let $\alpha$ be a finite search space and
$M \subseteq \alpha$ a marked set with complement $M^c$. For a real number $\varphi$, this is the
real amplitude vector on $\alpha$ whose value is $\sin\varphi / \sqrt{|M|}$ at every point of $M$
and $\cos\varphi / \sqrt{|M^c|}$ at every point of $M^c$.

When $M$ and $M^c$ are nonempty, the marked and unmarked parts of this vector have Euclidean
norms $|\sin\varphi|$ and $|\cos\varphi|$.

Formalized by `Cslib.Grover.angleAmplitude`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#angle-amplitude).

## Grover iterate

Let $\alpha$ be a finite search space and $M \subseteq \alpha$ a marked
set. For $k \in \mathbb{N}$ and a real amplitude vector $\psi : \alpha \to \mathbb{R}$, the $k$-th
Grover iterate of $\psi$ is the vector obtained by applying the Grover step for $M$ to $\psi$
$k$ times; the $0$-th iterate is $\psi$ itself.

Formalized by `Cslib.Grover.groverIterate`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#grover-iterate).

## Grover iteration preserves the squared norm

Let $\alpha$ be a nonempty finite search
space and $M \subseteq \alpha$ a marked set. For every real amplitude vector
$\psi : \alpha \to \mathbb{R}$ and every $k \in \mathbb{N}$, let $\psi_k$ be the vector obtained
from $\psi$ by applying the Grover step for $M$ $k$ times. Then
$\sum_{x \in \alpha} \psi_k(x)^2 = \sum_{x \in \alpha} \psi(x)^2$.

Formalized by `Cslib.Grover.amplitudeNormSq_groverIterate`, a theorem declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#amplitude-norm-sq-grover-iterate).

## Grover iterates of the uniform state are unit vectors

Let $\alpha$ be a nonempty finite
search space, $M \subseteq \alpha$ a marked set, and $u$ the uniform amplitude vector, given by
$u(x) = 1/\sqrt{|\alpha|}$ for every $x \in \alpha$. For every $k \in \mathbb{N}$, let $\psi_k$
be the vector obtained from $u$ by applying the Grover step for $M$ $k$ times. Then
$\sum_{x \in \alpha} \psi_k(x)^2 = 1$.

Formalized by `Cslib.Grover.amplitudeNormSq_groverIterate_uniform`, a theorem declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#amplitude-norm-sq-grover-iterate-uniform).

## Grover phase

Let $\alpha$ be a finite search space, $M \subseteq \alpha$ a marked set and
$\theta$ the Grover angle of $M$. For $k \in \mathbb{N}$, the Grover phase of $M$ after $k$
iterations is the real number $(2k + 1)\theta$.

When $M$ and its complement are both nonempty, this is the phase reached from the uniform
initial state after $k$ Grover steps.

Formalized by `Cslib.Grover.groverPhase`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#grover-phase).

## Exact success probability of Grover search

Let $\alpha$ be a finite search space and
$M \subseteq \alpha$ a marked set such that both $M$ and its complement are nonempty, and let
$\theta = \arcsin \sqrt{|M| / |\alpha|}$ be the Grover angle of $M$. For $k \in \mathbb{N}$, let
$\psi_k$ be the vector obtained by applying the Grover step for $M$ $k$ times to the uniform
amplitude vector, whose value is $1/\sqrt{|\alpha|}$ at every point. Then the marked probability
of $\psi_k$ is $\sum_{x \in M} \psi_k(x)^2 = \sin^2((2k + 1)\theta)$.

Formalized by `Cslib.Grover.markedProbability_groverIterate_uniform`, a theorem declared in [CSLibExt/Algorithms/Quantum/Grover/Analysis.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/Analysis.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#marked-probability-grover-iterate-unifor).

## Standard Grover iteration count

Let $M$ be a set of marked elements of a finite search
space of size $N$, and let $\theta = \arcsin \sqrt{|M| / N}$ be its Grover angle. The standard
iteration count is $\lfloor \pi / (4\theta) \rfloor$, the largest natural number at most
$\pi / (4\theta)$; it is $0$ when $\theta = 0$, that is, when no element is marked.

Formalized by `Cslib.Grover.floorIterations`, a definition declared in [CSLibExt/Algorithms/Quantum/Grover/IterationBounds.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/IterationBounds.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#floor-iterations).

## One Grover iteration suffices when a quarter is marked

Let $M$ be a nonempty set of
marked elements of a finite search space of size $N$ with $4|M| = N$. Starting from the uniform
amplitude vector, one Grover iteration produces an amplitude vector whose marked probability
is $1$.

Formalized by `Cslib.Grover.one_step_success_of_four_mul_card_eq`, a theorem declared in [CSLibExt/Algorithms/Quantum/Grover/IterationBounds.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Quantum/Grover/IterationBounds.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html#one-step-success-of-four-mul-card-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Grover's algorithm](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/quantum-algorithms/grover-s-algorithm)
