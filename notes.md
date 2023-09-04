# Property Based Testing in Python

Quick review of unit testing
* Happy paths


The issues with unit testing
* Testing every input is boring
* Thinking of every edge case is hard & error-prone

Introduce Hypothesis
* We generate code, why not generate tests?

Refactor unit tests with Hypothesis

Introduce Properties

Thinking of Properties (att: ScottW, FSharp for Fun and Profit)
* Different paths, same destination - A diagram that commutes
* There and back again - an invertible function
* Some things never change - an invariant under transformation
* The more things change, the more they stay the same - idempotence
* Solve a smaller problem first - structural induction
* Hard to prove, easy to verify
* A test oracle

Properties vs Fuzzing
* Testing random values to see if something fails vs testing properties to check the specification of a program

Vocabulary
* Properties
* Generators
* Shrinkers

Issues with property based testing
* They are slower (they run more tests)
* Test pipelines become non-deterministic (failures are good to find, but re-running CI can pass then fail!)
* Writing good properties is hard
* Writing enough properties is hard

Testing libraries (not exhaustive)
* Python - Hypothesis
* .NET - FsCheck
* JVM - jqwik/ScalaCheck
* Erlang/Elixir - PropEr
* The OG - Haskell QuickCheck

