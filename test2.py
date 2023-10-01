import proc


proc LS_3_Opt(tour: var Tour_Array) =
  ## Iteratively optimizes given tour using 3-opt moves.
  # Shortens the tour by repeating 3-opt moves until no improvement
  # can by done; in every iteration immediatelly makes permanent
  # change from the first move found that gives any length gain.
  var
    locallyOptimal: bool = false
    i, j, k: Tour_Index
    X1, X2, Y1, Y2, Z1, Z2: City_Number
    optCase: Reconnection_3_optCase
    gainExpected: Length_Gain

  while not locallyOptimal:
    locallyOptimal = true

    block four_loops:
      for counter_1 in 0 .. N-1:
        i = counter_1 # first cut after i
        X1 = tour[i]
        X2 = tour[(i+1) mod N]
        for counter_2 in 1 .. N-3:
          j = (i + counter_2) mod N # second cut after j
          Y1 = tour[j]
          Y2 = tour[(j+1) mod N]
          for counter_3 in counter_2+1 .. N-1:
            k = (i + counter_3) mod N  # third cut after k
            Z1 = tour[k]
            Z2 = tour[(k+1) mod N]

            for optCase in [opt3_case_3, opt3_case_6, opt3_case_7]:
              gainExpected = Gain_From_3_Opt(X1, X2,
                                             Y1, Y2,
                                             Z1, Z2,
                                             optCase)
              if gainExpected > 0:
                Make_3_Opt_Move(tour, i, j, k, optCase)
                locallyOptimal = false
                break four_loops