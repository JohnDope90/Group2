def IdRule(model_path):
    ## Dataframe (table) so we can correlate coordinates and ID for the relevant stairs ##
    # Dataframe contains all stairs in model
    df = pd.DataFrame(stair_coords, columns = ["x", "y", "z"])
    # Taking IDs for all stairs and adding the column to the coordinate table
    IDs = []
    for stair in stairs:
        IDs.append(stair.GlobalId)

    # Adding "IDs" column to df (dataframe)
    df['Global_ID'] = IDs

    # print(df,"\n")


    ## Taking relevant stairs' coordinates and finding their corresponding IDs ##

    row_num = ()

    for rel_stairs in filtered_stairways:
        for stair in rel_stairs:
            in_array = df[(df["x"] == stair[0]) & (df["y"] == stair[1])].index.to_numpy()
            row_num = np.append(row_num, in_array)

    row_num = np.unique(row_num).astype(int)
    #row_num = df[(df["x"] == filtered_stairways[0][3][0]) & (df["y"] == filtered_stairways[0][3][1]) & (df["z"] == filtered_stairways[0][3][2])]

    # row_num = df[(df["x"] == filtered_stairways[0][3][0]) & (df["y"] == filtered_stairways[0][3][1]) & (df["z"] == filtered_stairways[0][3][2])].index.tolist()
    print(f"Row numbers for relevant stairs:\n {row_num}.\n")

    print(f"Amount of relevant stairs found: {len(row_num)}")

    ID_list=[]
    for number in row_num:
        inlist = (df.iloc[number][3])
        ID_list.append(inlist)
        
    return ID_list
