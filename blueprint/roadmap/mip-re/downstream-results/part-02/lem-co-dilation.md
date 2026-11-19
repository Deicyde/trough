---
declaration: lemma
origin: cited
lean: MIPRE.OperatorMatrix.toCLMStarAlgHom, MIPRE.OperatorMatrix.amplify, MIPRE.OperatorMatrix.emb, MIPRE.OperatorMatrix.inner_emb_toCLM_emb, MIPRE.OperatorMatrix.toCLM_diagonal_emb, MIPRE.Halmos.extension, MIPRE.Halmos.conjTranspose_mul_extension, MIPRE.Halmos.extension_mul_conjTranspose, MIPRE.Halmos.naimark, MIPRE.Halmos.naimark_mul_conjTranspose_mul, MIPRE.Halmos.proj, MIPRE.Halmos.isStarProjection_proj, MIPRE.Halmos.sum_proj, MIPRE.Halmos.proj_naimark_inl_inl, MIPRE.Halmos.commute_diagonal_proj_naimark, MIPRE.CommutingOperatorStrategy.dilateLeft, MIPRE.CommutingOperatorStrategy.correlation_dilateLeft, MIPRE.CommutingOperatorStrategy.swap, MIPRE.CommutingOperatorStrategy.correlation_swap, MIPRE.CommutingOperatorStrategy.dilateRight, MIPRE.CommutingOperatorStrategy.correlation_dilateRight
statement: formalized
proof: formalized
---

# Commutation-preserving dilation

Let $\{E_a\}_{a \in {\mathcal{A}}}$ be a POVM on a Hilbert space $\mathcal{H}$, let $a_0 \in {\mathcal{A}}$, and let $\iota : \mathcal{H} \to \mathcal{H} \otimes (\mathbb{C}^{{\mathcal{A}}} \oplus \mathbb{C}^{{\mathcal{A}}})$ be the embedding $\xi \mapsto \xi \otimes e_{a_0}$ at the first copy of $a_0$. There is a projective measurement $\{P_a\}_{a \in {\mathcal{A}}}$ on $\mathcal{H} \otimes (\mathbb{C}^{{\mathcal{A}}} \oplus \mathbb{C}^{{\mathcal{A}}})$ such that

1. $\iota^* P_a \iota = E_a$ for every $a$, and
2. $P_a$ commutes with $c \otimes {I}$ for every bounded operator $c$ on $\mathcal{H}$ that commutes with every $E_b$.

Consequently, for a commuting-operator strategy $\mathscr{S} = (\mathcal{H}, \psi, E, F)$ and a question $x$ of the first player, the strategy on $\mathcal{H} \otimes (\mathbb{C}^{{\mathcal{A}}} \oplus \mathbb{C}^{{\mathcal{A}}})$ with state $\iota(\psi)$, in which the first player measures the $\{P_a\}$ of $\{E^x_a\}_a$ at $x$ and $E^{x'}_a \otimes {I}$ at $x' \neq x$ and the second player measures $F^y_b \otimes {I}$, is a commuting-operator strategy with the correlation of $\mathscr{S}$. Its measurement at $x$ is projective, and so is every measurement that was projective in $\mathscr{S}$. The same holds for a question of the second player.

## Depends on

- [Commuting-operator strategy](../../parallel-repetition/def-co-strategy-bipartite.md)

## Proof

Let $s_a = \sqrt{E_a}$, by the continuous functional calculus: it is self-adjoint, $\sum_a s_a^2 = {I}$, and it commutes with every operator that commutes with $E_a$. Write operators on $\mathcal{H} \otimes \mathbb{C}^n$ as $n \times n$ matrices of operators on $\mathcal{H}$, so that composition and the adjoint are the matrix product and the conjugate transpose. Let $W$ be the ${\mathcal{A}} \times {\mathcal{A}}$ matrix whose column $a_0$ is $(s_a)_a$ and whose other columns vanish. Then $W^* W$ is the matrix unit at $(a_0, a_0)$, so $W W^* W = W$ and $W$ is a partial isometry. The block matrix

$$
U = \begin{pmatrix} W & {I} - W W^* \\ {I} - W^* W & W^* \end{pmatrix}
$$

is unitary, by the identities $W({I} - W^* W) = 0$ and $({I} - W W^*) W = 0$ and their adjoints. Let $Q_a$ be the diagonal projection onto the two copies of the coordinate $a$, and put $P_a = U^* Q_a U$. These are projections summing to ${I}$, and the entry of $P_a$ at the first copy of $(a_0, a_0)$ is $s_a s_a = E_a$, which is item 1. Every entry of $U$ is a polynomial in the $s_b$, and so commutes with $c$ as soon as $c$ commutes with every $E_b$, which is item 2.

For the strategy, take $c = F^y_b$. The correlation at $(x, y)$ is $\langle\iota\psi| P_a (F^y_b \otimes {I}) |\iota\psi\rangle = \langle\psi| \iota^* P_a \iota F^y_b |\psi\rangle$, because $(F^y_b \otimes {I}) \iota = \iota F^y_b$, and item 1 makes it $\langle\psi| E^x_a F^y_b |\psi\rangle$. At $x' \neq x$ both operators are amplified, and $\iota$ is an isometry. The amplification $c \mapsto c \otimes {I}$ is a unital $*$-homomorphism, so it preserves positivity, sums to ${I}$, commutation and idempotence. For the second player, exchange the players, which transposes the correlation because the two players' operators commute.

## Lean

Formalized as [`MIPRE.OperatorMatrix.toCLMStarAlgHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.toCLMStarAlgHom), [`MIPRE.OperatorMatrix.amplify`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.amplify), [`MIPRE.OperatorMatrix.emb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.emb), [`MIPRE.OperatorMatrix.inner_emb_toCLM_emb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.inner_emb_toCLM_emb), [`MIPRE.OperatorMatrix.toCLM_diagonal_emb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.OperatorMatrix.toCLM_diagonal_emb), [`MIPRE.Halmos.extension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.extension), [`MIPRE.Halmos.conjTranspose_mul_extension`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.conjTranspose_mul_extension), [`MIPRE.Halmos.extension_mul_conjTranspose`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.extension_mul_conjTranspose), [`MIPRE.Halmos.naimark`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.naimark), [`MIPRE.Halmos.naimark_mul_conjTranspose_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.naimark_mul_conjTranspose_mul), [`MIPRE.Halmos.proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.proj), [`MIPRE.Halmos.isStarProjection_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.isStarProjection_proj), [`MIPRE.Halmos.sum_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.sum_proj), [`MIPRE.Halmos.proj_naimark_inl_inl`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.proj_naimark_inl_inl), [`MIPRE.Halmos.commute_diagonal_proj_naimark`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Halmos.commute_diagonal_proj_naimark), [`MIPRE.CommutingOperatorStrategy.dilateLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.dilateLeft), [`MIPRE.CommutingOperatorStrategy.correlation_dilateLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.correlation_dilateLeft), [`MIPRE.CommutingOperatorStrategy.swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.swap), [`MIPRE.CommutingOperatorStrategy.correlation_swap`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.correlation_swap), [`MIPRE.CommutingOperatorStrategy.dilateRight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.dilateRight), [`MIPRE.CommutingOperatorStrategy.correlation_dilateRight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.correlation_dilateRight).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1096](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1096)
