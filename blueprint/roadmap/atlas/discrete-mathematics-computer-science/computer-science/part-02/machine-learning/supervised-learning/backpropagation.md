---
declaration: section
origin: cited
lean: Cslib.MachineLearning.Backpropagation.Net, Cslib.MachineLearning.Backpropagation.Net.forward, Cslib.MachineLearning.Backpropagation.Net.backward, Cslib.MachineLearning.Backpropagation.Net.DiffAlong, Cslib.MachineLearning.Backpropagation.Net.diffAlong_of_differentiable, Cslib.MachineLearning.Backpropagation.Net.differentiableAt_forward, Cslib.MachineLearning.Backpropagation.Net.backward_eq, Cslib.MachineLearning.Backpropagation.gradient_comp_forward
statement: formalized
proof: formalized
---

# Backpropagation

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html).

## Feedforward network

Given layer widths $d : \mathbb{N} \to \mathbb{N}$, a feedforward
network with widths $d$ is a sequence of arbitrary maps
$f_k : \mathbb{R}^{d(k)} \to \mathbb{R}^{d(k+1)}$, one for each $k \in \mathbb{N}$, where $f_k$ is
the map computed by layer $k$ and $\mathbb{R}^n$ carries its Euclidean structure.

Formalized by `Cslib.MachineLearning.Backpropagation.Net`, a structure declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#net).

## The forward pass

For a feedforward network with layers
$f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, the forward pass
through the first $n$ layers is the map $N_n : \mathbb{R}^{d_0} \to \mathbb{R}^{d_n}$ given by
$N_0(x) = x$ and $N_{n+1}(x) = f_n(N_n(x))$, that is, $N_n = f_{n-1} \circ \cdots \circ f_0$.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.forward`, a definition declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#forward).

## The backward pass

Let $N$ be a feedforward network with layers
$f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, let
$x \in \mathbb{R}^{d_0}$ be an input, and write $a_k \in \mathbb{R}^{d_k}$ for the forward pass of
$x$ through the first $k$ layers. For each $n \in \mathbb{N}$, the backward pass at $x$ sends a
vector $\delta \in \mathbb{R}^{d_n}$ to $B_n(\delta) \in \mathbb{R}^{d_0}$, defined by
$B_0(\delta) = \delta$ and $B_{n+1}(\delta) = B_n(Df_n(a_n)^* \, \delta)$, where $Df_n(a_n)$ is the
Fréchet derivative of $f_n$ at $a_n$ (taken to be $0$ if $f_n$ is not differentiable there) and
$^*$ denotes the adjoint. Thus
$B_n(\delta) = Df_0(a_0)^* \cdots Df_{n-1}(a_{n-1})^* \, \delta$: the adjoints of the layer
Jacobians are applied from the last layer to the first.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.backward`, a definition declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#backward).

## Differentiability along the forward pass

Let $N$ be a feedforward network with layers
$f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, let
$x \in \mathbb{R}^{d_0}$ and $n \in \mathbb{N}$, and write $a_j \in \mathbb{R}^{d_j}$ for the
forward pass of $x$ through the first $j$ layers. The network is differentiable along the forward
pass of $x$ through its first $n$ layers when $f_j$ is differentiable at $a_j$ for every
$j < n$.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.DiffAlong`, a definition declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#diff-along).

## Differentiable layers are differentiable along every forward pass

Let $N$ be a
feedforward network with layers $f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between
Euclidean spaces. If every $f_k$ is differentiable on all of $\mathbb{R}^{d_k}$, then for every
input $x \in \mathbb{R}^{d_0}$ and every $n \in \mathbb{N}$, the layer $f_j$ is differentiable at
the forward pass of $x$ through the first $j$ layers for every $j < n$.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.diffAlong_of_differentiable`, a theorem declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#diff-along-of-differentiable).

## Differentiability of the forward pass

Let $N$ be a feedforward network with layers
$f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, let
$x \in \mathbb{R}^{d_0}$ and $n \in \mathbb{N}$, and write
$N_j : \mathbb{R}^{d_0} \to \mathbb{R}^{d_j}$ for the forward pass through the first $j$ layers. If
$f_j$ is differentiable at $N_j(x)$ for every $j < n$, then $N_n$ is differentiable at $x$.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.differentiableAt_forward`, a theorem declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#differentiable-at-forward).

## The backward pass is the vector-Jacobian product

Let $N$ be a feedforward network with
layers $f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, let
$x \in \mathbb{R}^{d_0}$ and $n \in \mathbb{N}$, and write
$N_j : \mathbb{R}^{d_0} \to \mathbb{R}^{d_j}$ for the forward pass through the first $j$ layers. If
$f_j$ is differentiable at $N_j(x)$ for every $j < n$, then for every $\delta \in \mathbb{R}^{d_n}$
the backward pass from $\delta$ at input $x$ through the first $n$ layers equals
$DN_n(x)^* \, \delta$, where $DN_n(x)$ is the Fréchet derivative of $N_n$ at $x$ and $^*$ denotes
the adjoint.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.backward_eq`, a theorem declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#backward-eq).

## Backpropagation computes the input gradient

Let $N$ be a feedforward network with layers
$f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, let
$x \in \mathbb{R}^{d_0}$ and $n \in \mathbb{N}$, and write $N_j$ for the forward pass through the
first $j$ layers. Assume that $f_j$ is differentiable at $N_j(x)$ for every $j < n$, and let
$\ell : \mathbb{R}^{d_n} \to \mathbb{R}$ be differentiable at $N_n(x)$. Then
$\nabla(\ell \circ N_n)(x)$ is the backward pass of $\nabla \ell(N_n(x))$ at input $x$ through
the first $n$ layers, that is,
$\nabla(\ell \circ N_n)(x) = Df_0(N_0(x))^* \cdots Df_{n-1}(N_{n-1}(x))^* \, \nabla \ell(N_n(x))$,
where $Df_j(N_j(x))$ is the Fréchet derivative of $f_j$ at $N_j(x)$ and $^*$ denotes the
adjoint.

Formalized by `Cslib.MachineLearning.Backpropagation.gradient_comp_forward`, a theorem declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#gradient-comp-forward).

## Shifted network

For a feedforward network $N$ with layer widths $d$ and a natural number
$j$, the shifted network has layer widths $i \mapsto d(j + i)$, and its layer $i$ is layer
$j + i$ of $N$. It is made of the layers of $N$ from layer $j$ on.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.shift`, a definition declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#shift).

## Splitting the forward pass

Let $N$ be a feedforward network with layers
$f_k : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ between Euclidean spaces, write $N_n$ for its
forward pass through the first $n$ layers, and for $j \in \mathbb{N}$ write $N^{(j)}_m$ for the
forward pass through the first $m$ layers of the shifted network with layers
$f_j, f_{j+1}, \dots$. Then for all $j, m \in \mathbb{N}$ and $x \in \mathbb{R}^{d_0}$,
$N_{j+m}(x) = N^{(j)}_m(N_j(x))$.

Formalized by `Cslib.MachineLearning.Backpropagation.Net.forward_add`, a theorem declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#forward-add).

## Parametrized feedforward network

Given layer widths $d : \mathbb{N} \to \mathbb{N}$ and
parameter dimensions $p : \mathbb{N} \to \mathbb{N}$, a parametrized network is a sequence of
arbitrary maps $f_k : \mathbb{R}^{p(k)} \times \mathbb{R}^{d(k)} \to \mathbb{R}^{d(k+1)}$, one for
each $k \in \mathbb{N}$: layer $k$ sends parameters $\theta \in \mathbb{R}^{p(k)}$ and an input
$x \in \mathbb{R}^{d(k)}$ to $f_k(\theta, x)$.

Formalized by `Cslib.MachineLearning.Backpropagation.PNet`, a structure declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#pnet).

## The network at fixed parameters

Let $P$ be a network with parameters whose layer $k$ is a
map $g_k : \mathbb{R}^{p_k} \times \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$ of the parameters
and the input (all spaces Euclidean). For parameters $\theta = (\theta_k)_{k \in \mathbb{N}}$ with
$\theta_k \in \mathbb{R}^{p_k}$, the network at $\theta$ is the feedforward network whose layer
$k$ is $g_k(\theta_k, \cdot) : \mathbb{R}^{d_k} \to \mathbb{R}^{d_{k+1}}$.

Formalized by `Cslib.MachineLearning.Backpropagation.PNet.net`, a definition declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#net-2).

## Backpropagation computes the parameter gradients

Let $P$ be a network with parameters
whose layer $i$ is a map $g_i : \mathbb{R}^{p_i} \times \mathbb{R}^{d_i} \to \mathbb{R}^{d_{i+1}}$
of the parameters and the input (all spaces Euclidean). Fix parameters $\theta = (\theta_i)_i$
with $\theta_i \in \mathbb{R}^{p_i}$, let $N$ be the network with layers
$f_i = g_i(\theta_i, \cdot)$, let $x \in \mathbb{R}^{d_0}$ and $k, m \in \mathbb{N}$, set
$L = k + 1 + m$, and write $a_j$ for the forward pass of $x$ through the first $j$ layers of $N$.
Assume that $f_{k+1+i}$ is differentiable at $a_{k+1+i}$ for every $i < m$, that
$h(t) = g_k(t, a_k)$ is differentiable at $\theta_k$, and that
$\ell : \mathbb{R}^{d_L} \to \mathbb{R}$ is differentiable at $a_L$. For
$t \in \mathbb{R}^{p_k}$ let $\Phi(t)$ be the forward pass of $x$ through the first $L$ layers of
the network obtained by replacing $\theta_k$ with $t$. Then

$$\nabla(\ell \circ \Phi)(\theta_k) = Dh(\theta_k)^* \, \delta,$$

where $\delta = Df_{k+1}(a_{k+1})^* \cdots Df_{L-1}(a_{L-1})^* \, \nabla \ell(a_L)$ (so
$\delta = \nabla \ell(a_L)$ when $m = 0$) is the backward pass of $\nabla \ell(a_L)$ through
layers $k + 1, \dots, L - 1$ of $N$, $D$ denotes the Fréchet derivative and $^*$ the adjoint.

Formalized by `Cslib.MachineLearning.Backpropagation.gradient_param`, a theorem declared in [CSLibExt/MachineLearning/Backpropagation.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/MachineLearning/Backpropagation.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html#gradient-param).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Backpropagation](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/machine-learning/supervised-learning/backpropagation)
